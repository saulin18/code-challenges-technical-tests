Formulario con useActionState
Un formulario de registro que hoy usa useState + onSubmit. Migra la lógica a useActionState para centralizar estado, validaciones y pending en un solo lugar — sin useState extra.

Objetivos
1.
Crea una función action async que recibe (prevState, formData)
2.
Valida username (mín 3 chars) y email (debe contener @) y retorna { error }
3.
Si es válido, retorna { ok: true, username }
4.
Conecta la action a useActionState y usa formAction como atributo action del form
5.
Deshabilita los inputs y el botón mientras isPending es true