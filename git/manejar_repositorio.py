from PIL import Image

''' Crear una copia local de un repositorio '''
# git clone /path/to/repository

''' Si utilizas un servidor remoto, ejecuta '''
# git clone username@host:/path/to/repository

# --------------------------- TREES --------------------

''' Tu repositorio local esta compuesto por tres "�rboles" administrados
por git. El primero es tu Directorio de trabajo que contiene los archivos,
el segundo es el Index que actua como una zona intermedia, y el �ltimo
es el HEAD que apunta al �ltimo commit realizado. '''

im = Image.open('trees.png')
# im.show()

''' Puedes registrar cambios (a�adirlos al Index) usando '''
# git add <filename>
# git add .

''' Este es el primer paso en el flujo de trabajo b�sico.
Para hacer commit a estos cambios usa '''
# git commit -m "Commit message"

''' Ahora el archivo esta inclu�do en el HEAD, pero a�n no
en tu repositorio remoto. '''

''' Tus cambios est�n ahora en el HEAD de tu copia local.
Para enviar estos cambios a tu repositorio remoto ejecuta '''
# git push origin master

''' Reemplaza master por la rama a la que quieres enviar tus cambios. '''

'''Si no has clonado un repositorio ya existente y quieres
conectar tu repositorio local a un repositorio remoto, usa '''
# git remote add origin <server>

''' Ahora podr�s subir tus cambios al repositorio remoto seleccionado. '''

# ----------------------- BRANCHES ----------------------

''' Las ramas son utilizadas para desarrollar funcionalidades
aisladas unas de otras. La rama master es la rama "por defecto"
cuando creas un repositorio. Crea nuevas ramas durante el desarrollo
y fusi�nalas a la rama principal cuando termines. '''

im = Image.open('branches.png')
# im.show()

''' Crea una nueva rama llamada "feature_x" y c�mbiate a ella usando '''
# git checkout -b feature_x

''' vuelve a la rama principal '''
# git checkout master
''' y borra la rama '''
# git branch -d feature_x

''' Una rama nueva no estar� disponible para los dem�s
a menos que subas (push) la rama a tu repositorio remoto '''
# git push origin <branch>

# ---------------- ACTUALIZAR Y FUSIONAR --------------------

''' Para actualizar tu repositorio local al commit m�s nuevo: ''' 
# git pull

''' en tu directorio de trabajo para bajar y fusionar los cambios remotos. '''

''' Para fusionar otra rama a tu rama activa (por ejemplo master): '''
# git merge <branch>

''' en ambos casos git intentar� fusionar autom�ticamente
los cambios. Desafortunadamente, no siempre ser� posible y se podr�n
producir conflictos. T� eres responsable de fusionar esos
conflictos manualmente al editar los archivos mostrados por git.
Despu�s de modificarlos, necesitas marcarlos como fusionados con '''
# git add <filename>

''' Antes de fusionar los cambios, puedes revisarlos usando '''
# git diff <source_branch> <target_branch>

# ------------------- ETIQUETAS ----------------------------

''' Se recomienda crear etiquetas para cada nueva versi�n
publicada de un software. Puedes crear una nueva etiqueta
llamada 1.0.0 ejecutando '''
# git tag 1.0.0 1b2e1d63ff

''' 1b2e1d63ff se refiere a los 10 caracteres del commit id
al cual quieres referirte con tu etiqueta.
Puedes obtener el commit id con '''
# git log

''' tambi�n puedes usar menos caracteres que el commit id,
pero debe ser un valor �nico. '''

# --------------- REEMPLAZAR CAMBIOS LOCALES -----------------

''' En caso de que hagas algo mal  puedes reemplazar
cambios locales usando el comando '''
# git checkout -- <filename>

''' Este comando reemplaza los cambios en tu directorio de trabajo
con el �ltimo contenido de HEAD. Los cambios que ya han sido
agregados al Index, as� como tambi�n los nuevos archivos,
se mantendr�n sin cambio. '''

''' Por otro lado, si quieres deshacer todos los cambios locales
y commits, puedes traer la �ltima versi�n del servidor y apuntar
a tu copia local principal de esta forma '''
# git fetch origin
# git reset --hard origin/master
