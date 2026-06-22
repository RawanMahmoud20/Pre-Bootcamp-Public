const CSRF = document.cookie.match(/csrftoken=([^;]+)/)?.[1] || '';

function createCategory() {
  const name = document.getElementById('new-cat-name').value.trim();
  const errEl = document.getElementById('cat-error');
  const sucEl = document.getElementById('cat-success');
  errEl.classList.add('d-none');
  sucEl.classList.add('d-none');

  if (!name) {
    errEl.textContent = 'Name is required.';
    errEl.classList.remove('d-none');
    return;
  }

  fetch('/api/categories/create/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json', 'X-CSRFToken': CSRF},
    body: JSON.stringify({name})
  })
  .then(r => r.json())
  .then(data => {
    if (data.error) {
      errEl.textContent = data.error;
      errEl.classList.remove('d-none');
      return;
    }

    const empty = document.getElementById('cat-empty');
    if (empty) empty.remove();

    const li = document.createElement('li');
    li.className = 'list-group-item d-flex justify-content-between align-items-center';
    li.id = `cat-item-${data.category.id}`;
    li.innerHTML = `<span><i class="bi bi-tag me-2 text-info"></i>${data.category.name}</span>
      <button class="btn btn-sm btn-outline-danger" onclick="deleteCategory(${data.category.id}, '${data.category.name}')">
        <i class="bi bi-trash3"></i>
      </button>`;
    document.getElementById('cat-list').appendChild(li);

    addCatCheckbox(data.category.id, data.category.name);

    sucEl.textContent = `Category "${data.category.name}" added!`;
    sucEl.classList.remove('d-none');
    document.getElementById('new-cat-name').value = '';
  });
}

function deleteCategory(pk, name) {
  if (!confirm(`Delete category "${name}"?`)) return;

  fetch(`/api/categories/${pk}/delete/`, {
    method: 'POST',
    headers: {'X-CSRFToken': CSRF}
  })
  .then(r => r.json())
  .then(data => {
    if (data.success) {
      document.getElementById(`cat-item-${pk}`)?.remove();
      document.getElementById(`newcat${pk}`)?.closest('.form-check')?.remove();
      document.getElementById(`editcat${pk}`)?.closest('.form-check')?.remove();
    }
  });
}

function addCatCheckbox(id, name) {
  const newContainer = document.getElementById('new-cat-container');
  const editContainer = document.getElementById('edit-cat-container');

  const makeCheck = (prefix) => {
    const div = document.createElement('div');
    div.className = 'form-check form-check-inline';
    div.innerHTML = `<input class="form-check-input ${prefix}-cat-check" type="checkbox" value="${id}" id="${prefix}cat${id}" />
      <label class="form-check-label" for="${prefix}cat${id}">${name}</label>`;
    return div;
  };

  if (newContainer) {
    document.getElementById('new-cat-empty')?.remove();
    newContainer.appendChild(makeCheck('new'));
  }
  if (editContainer) editContainer.appendChild(makeCheck('edit'));
}