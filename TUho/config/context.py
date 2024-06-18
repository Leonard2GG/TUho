# Context Processors
<<<<<<< HEAD
from usuarios.models import Usuario
=======
from apps.Usuarios.models import Usuario
>>>>>>> 84284b3abc174c92c9d1701f14501b1ac71047e7
def groups_processor(request) -> dict:
    if request.user.is_authenticated:
        grupos = Usuario.objects.get(id=request.user.id).groups.all()
        return { 'grupos': [e.name for e in grupos] }
    return {}

