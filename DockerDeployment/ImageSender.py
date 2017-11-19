from PIL import Image
from StringIO import StringIO


class ImageSender():

    @staticmethod
    def prepare_to_send(image):
        pil_im = Image.fromarray(image)
        io = StringIO()
        pil_im.save(io, "jpeg")
        ret = io.getvalue()
        io.close()
        return ret

