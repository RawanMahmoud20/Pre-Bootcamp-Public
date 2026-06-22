/* ========================================================
   Smart Task Manager – AJAX interaction engine
   Handles: status updates, task creation, editing,
            deletion, client-side filtering & search.
   ======================================================== */

'use strict';

// ---- CSRF helper ----
function getCsrfToken() {
  const cookie = document.cookie.split(';').find(c => c.trim().startsWith('csrftoken='));
  return cookie ? cookie.trim().split('=')[1] : '';
}

function jsonPost(url, body) {
  return fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCsrfToken(),
    },
    body: JSON.stringify(body),
  });
}

// ---- Toast ----
function showToast(message, type = 'success') {
  const toast = document.getElementById('toast-notify');
  const msg   = document.getElementById('toast-msg');
  if (!toast || !msg) return;
  toast.classList.remove('bg-success', 'bg-danger', 'bg-warning');
  toast.classList.add(type === 'success' ? 'bg-success' : type === 'warning' ? 'bg-warning' : 'bg-danger');
  msg.textContent = message;
  bootstrap.Toast.getOrCreateInstance(toast, { delay: 3000 }).show();
}

// ---- Status update (inline dropdown) ----
function updateStatus(taskId, newStatus, event) {
  event.preventDefault();
  jsonPost(`/api/tasks/${taskId}/status/`, { status: newStatus })
    .then(r => r.json())
    .then(data => {
      if (data.success) {
        showToast(`Status set to "${newStatus}".`);
        refreshTaskCard(taskId, data.task);
        syncFilterVisibility();
      } else {
        showToast(data.error || 'Failed to update status.', 'danger');
      }
    })
    .catch(() => showToast('Network error.', 'danger'));
}

// ---- Refresh a single card in-place ----
function refreshTaskCard(taskId, task) {
  // Simplest reliable approach: reload the list from the server
  // so the rendered card HTML is always in sync with Django templates.
reloadTaskList();
}

// ---- Reload full task list via AJAX ----
let currentStatusFilter = '';

function reloadTaskList() {
  const url = currentStatusFilter
    ? `/api/tasks/?status=${encodeURIComponent(currentStatusFilter)}`
    : '/api/tasks/';

  fetch(url)
    .then(r => r.json())
    .then(data => {
      renderTaskCards(data.tasks);
      syncFilterVisibility();
    })
    .catch(() => showToast('Could not refresh tasks.', 'danger'));
}

function renderTaskCards(tasks) {
  const list = document.getElementById('task-list');
  if (!list) return;

  if (tasks.length === 0) {
    list.innerHTML = `
      <div class="col-12" id="empty-state">
        <div class="card border-0 shadow-sm text-center py-5">
          <i class="bi bi-inbox display-4 text-muted d-block mb-3"></i>
          <p class="text-muted mb-3">No tasks yet. Click <strong>New Task</strong> to get started.</p>
        </div>
      </div>`;
    return;
  }

  list.innerHTML = tasks.map(t => {
    const statusBadge = t.status === 'Pending'
      ? 'bg-secondary'
      : t.status === 'In Progress'
      ? 'bg-warning text-dark'
      : 'bg-success';

    const statusIcon = t.status === 'Completed'
      ? '<i class="bi bi-check-circle-fill text-success fs-4"></i>'
      : t.status === 'In Progress'
      ? '<i class="bi bi-arrow-repeat text-warning fs-4 spin"></i>'
      : '<i class="bi bi-circle text-secondary fs-4"></i>';

    const cats = t.categories.map(c =>
      `<span class="badge bg-info-subtle text-info rounded-pill small">${escHtml(c)}</span>`
    ).join(' ');

    const catIdsArray = t.category_ids ? t.category_ids : []; 

    // تحويل البيانات لنصوص آمنة داخل الـ HTML لتجنب تضارب علامات التنصيص
    const safeTitle = escHtml(t.title).replace(/'/g, "&#39;");
    const safeDesc = escHtml(t.description || '').replace(/'/g, "&#39;");
    const safeDate = t.due_date ? t.due_date.substring(0, 16) : ''; // للتوافق مع datetime-local

    return `
    <div class="col-12 task-card-wrapper" data-status="${escHtml(t.status)}" data-title="${escHtml(t.title.toLowerCase())}">
      <div class="card border-0 shadow-sm task-card">
        <div class="card-body p-3 d-flex align-items-start gap-3">
          <div class="task-status-icon mt-1">${statusIcon}</div>
          <div class="flex-grow-1 min-w-0">
            <div class="d-flex justify-content-between align-items-start flex-wrap gap-1">
              <h6 class="mb-1 fw-semibold task-title">${escHtml(t.title)}</h6>
              <span class="badge rounded-pill ${statusBadge}">${escHtml(t.status)}</span>
            </div>
            ${t.description ? `<p class="text-muted small mb-1">${escHtml(t.description.substring(0,120))}${t.description.length > 120 ? '…' : ''}</p>` : ''}
            <div class="d-flex align-items-center gap-3 flex-wrap mt-1">
              <small class="text-muted"><i class="bi bi-calendar-event me-1"></i>${formatDate(t.due_date)}</small>
              ${cats}
            </div>
          </div>
          <div class="d-flex gap-1 flex-shrink-0 mt-1">
            <div class="dropdown">
              <button class="btn btn-sm btn-outline-primary dropdown-toggle" data-bs-toggle="dropdown" title="Change status">
                <i class="bi bi-arrow-left-right"></i>
              </button>
              <ul class="dropdown-menu dropdown-menu-end shadow border-0">
                <li><h6 class="dropdown-header text-muted">Set Status</h6></li>
                <li><a class="dropdown-item" href="#" onclick="updateStatus(${t.id}, 'Pending', event)"><i class="bi bi-circle me-2 text-secondary"></i>Pending</a></li>
                <li><a class="dropdown-item" href="#" onclick="updateStatus(${t.id}, 'In Progress', event)"><i class="bi bi-arrow-repeat me-2 text-warning"></i>In Progress</a></li>
                <li><a class="dropdown-item" href="#" onclick="updateStatus(${t.id}, 'Completed', event)"><i class="bi bi-check-circle me-2 text-success"></i>Completed</a></li>
              </ul>
            </div>
            
            <button class="btn btn-sm btn-outline-secondary" title="Edit"
                    onclick="openEditModal(${t.id}, '${safeTitle}', '${safeDesc}', '${safeDate}', ${JSON.stringify(catIdsArray)})">
              <i class="bi bi-pencil"></i>
            </button>
            
            <button class="btn btn-sm btn-outline-danger" title="Delete" onclick="deleteTask(${t.id})">
              <i class="bi bi-trash3"></i>
            </button>
          </div>
        </div>
      </div>
    </div>`;
  }).join('');
}

function escHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function formatDate(iso) {
  if (!iso) return '';
  const d = new Date(iso);
  return d.toLocaleString('en-US', { month: 'short', day: 'numeric', year: 'numeric', hour: 'numeric', minute: '2-digit' });
}

// ---- Filter buttons ----
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', function () {
    document.querySelectorAll('.filter-btn').forEach(b => {
      b.classList.remove('active', 'btn-primary', 'btn-secondary', 'btn-warning', 'btn-success');
      b.classList.add('btn-outline-secondary');
    });
    this.classList.remove('btn-outline-secondary', 'btn-outline-primary', 'btn-outline-warning', 'btn-outline-success');
    this.classList.add('active');

    currentStatusFilter = this.dataset.status;
    reloadTaskList();
  });
});

function syncFilterVisibility() {
  const search = (document.getElementById('search-input')?.value || '').toLowerCase();
  const wrappers = document.querySelectorAll('.task-card-wrapper');
  let visible = 0;

  wrappers.forEach(w => {
    const matchesStatus = !currentStatusFilter || w.dataset.status === currentStatusFilter;
    const matchesSearch = !search || (w.dataset.title || '').includes(search);
    const show = matchesStatus && matchesSearch;
    w.classList.toggle('hidden', !show);
    if (show) visible++;
  });

  const noResults = document.getElementById('no-results');
  if (noResults) noResults.classList.toggle('d-none', visible > 0);
}

function filterBySearch() {
  syncFilterVisibility();
}

// ---- Create task ----
document.getElementById('btn-create-task')?.addEventListener('click', () => {
  const title   = document.getElementById('new-title').value.trim();
  const desc    = document.getElementById('new-desc').value.trim();
  const due     = document.getElementById('new-due').value;
  const errBox  = document.getElementById('new-task-error');
  const catIds  = [...document.querySelectorAll('.new-cat-check:checked')].map(c => parseInt(c.value));

  errBox.classList.add('d-none');

  if (!title) { errBox.textContent = 'Title is required.'; errBox.classList.remove('d-none'); return; }
  if (!due)   { errBox.textContent = 'Due date is required.'; errBox.classList.remove('d-none'); return; }

  jsonPost('/api/tasks/create/', { title, description: desc, due_date: due, categories: catIds })
    .then(r => r.json())
    .then(data => {
      if (data.success) {
        bootstrap.Modal.getInstance(document.getElementById('modalNewTask')).hide();
        document.getElementById('new-title').value = '';
        document.getElementById('new-desc').value  = '';
        document.getElementById('new-due').value   = '';
        document.querySelectorAll('.new-cat-check').forEach(c => c.checked = false);
        showToast('Task created successfully!');
        reloadTaskList();
      } else {
        errBox.textContent = data.error || 'Failed to create task.';
        errBox.classList.remove('d-none');
      }
    })
    .catch(() => { errBox.textContent = 'Network error.'; errBox.classList.remove('d-none'); });
});

// ---- Edit task ----
function openEditModal(id, title, desc, due, catIds) {
  document.getElementById('edit-task-id').value  = id;
  document.getElementById('edit-title').value    = title;
  document.getElementById('edit-desc').value     = desc || '';
  document.getElementById('edit-due').value      = due;
  document.getElementById('edit-task-error').classList.add('d-none');

  document.querySelectorAll('.edit-cat-check').forEach(cb => {
    cb.checked = catIds.includes(parseInt(cb.value));
  });

  bootstrap.Modal.getOrCreateInstance(document.getElementById('modalEditTask')).show();
}

document.getElementById('btn-save-edit')?.addEventListener('click', () => {
  const id      = document.getElementById('edit-task-id').value;
  const title   = document.getElementById('edit-title').value.trim();
  const desc    = document.getElementById('edit-desc').value.trim();
  const due     = document.getElementById('edit-due').value;
  const errBox  = document.getElementById('edit-task-error');
  const catIds  = [...document.querySelectorAll('.edit-cat-check:checked')].map(c => parseInt(c.value));

  errBox.classList.add('d-none');

  if (!title) { errBox.textContent = 'Title is required.'; errBox.classList.remove('d-none'); return; }
  if (!due)   { errBox.textContent = 'Due date is required.'; errBox.classList.remove('d-none'); return; }

  jsonPost(`/api/tasks/${id}/edit/`, { title, description: desc, due_date: due, categories: catIds })
    .then(r => r.json())
    .then(data => {
      if (data.success) {
        bootstrap.Modal.getInstance(document.getElementById('modalEditTask')).hide();
        showToast('Task updated.');
        reloadTaskList();
      } else {
        errBox.textContent = data.error || 'Failed to save changes.';
        errBox.classList.remove('d-none');
      }
    })
    .catch(() => { errBox.textContent = 'Network error.'; errBox.classList.remove('d-none'); });
});

// ---- Delete task ----
function deleteTask(taskId) {
  if (!confirm('Delete this task? This cannot be undone.')) return;
  jsonPost(`/api/tasks/${taskId}/delete/`, {})
    .then(r => r.json())
    .then(data => {
      if (data.success) {
        showToast('Task deleted.', 'warning');
        reloadTaskList();
      } else {
        showToast(data.error || 'Delete failed.', 'danger');
      }
    })
    .catch(() => showToast('Network error.', 'danger'));
}
