from libs.http import render_json
from libs import errors

def yourname(request):
    name = request.POST.get("username")

    if name == "moson":
        return render_json(data="你好，Moson")
    else:
        return render_json(code=errors.PHONE_NUM_ERR)