# Permissions and Groups setup

This project uses the `bookshelf` app with custom permissions and groups.

## Custom permissions

In `bookshelf/models.py` on the `Book` model there is a `Meta` class with:

- `can_view`   – permission to view a book
- `can_create` – permission to create a book
- `can_edit`   – permission to edit a book
- `can_delete` – permission to delete a book

These permissions are created by Django migrations and can be assigned to users or groups from the admin site.

## Groups and usage

In the Django admin we can create groups such as:

- **Viewers** – get `can_view`
- **Editors** – get `can_view`, `can_create`, `can_edit`
- **Admins** – get all permissions including `can_delete`

The views that create, edit, or delete `Book` objects are protected with
`@permission_required` decorators in `bookshelf/views.py`, for example:

- `@permission_required("bookshelf.can_create", raise_exception=True)` for create
- `@permission_required("bookshelf.can_edit", raise_exception=True)` for edit
- `@permission_required("bookshelf.can_delete", raise_exception=True)` for delete

This way, access to each action is controlled by the custom permissions and the
groups a user belongs to.
