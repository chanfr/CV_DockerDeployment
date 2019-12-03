from io import BytesIO

from PIL import Image


class ImageSender():

    @staticmethod
    def prepare_to_send(image):
        pil_im = Image.fromarray(image)
        io = BytesIO()
        pil_im.save(io, "jpeg")
        ret = io.getvalue()
        io.close()
        return ret

