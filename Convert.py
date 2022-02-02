# Class Convert in Binary/Bytes
# PIL - to work with convert Bytes to Image
import PIL.Image as Image
from io import *
import base64


class convert:

    def __init__(self, path):
        self.path = path

    # https://www.kite.com/python/answers/how-to-read-a-file-byte-by-byte-and-print-a-list-of-bytes-in-binary-in-python
    def ImageToBytes(self):
        print("Converting started...")
        byte_list = []
        arrayToWrite = []
        with open(self.path, "rb") as in_file, open(self.path + "out_file.txt", "w") as out_file:
            while True:
                byte = in_file.read(1)
                if not byte:
                    break
                byte_list.append(byte)
            for i in range(len(byte_list)):
                arrayToWrite.append(str(ord(byte_list[i])))
            for j in range(len(arrayToWrite)):
                out_file.write(arrayToWrite[j] + " ")
        print("Success!")

    def BytesToImage(self):
        print("Converting started...")
        with open(self.path, "rb") as infile, open(self.path + "image.txt", "r+b") as image:
            try:
                byte = str((infile.read()).split())
                arrayOfBytes = bytearray(byte, encoding="utf8")
                source = Image.open(arrayOfBytes)
                source.save("image.png")
                print(arrayOfBytes)

            except Exception:
                print("ERROR!")

        print("Success!")

    def ImageToBinary(self):
        print("Converting started...")
        binary_list = []
        arrayToWrite = []
        with open(self.path, "rb") as infile, open(self.path + "out_file2.txt", "w") as out_file:
            while True:
                binary = infile.read(1)
                if not binary:
                    break
                binary_list.append(binary)
            for i in range(len(binary_list)):
                arrayToWrite.append(str(bin(ord(binary_list[i]))))
            for j in range(len(arrayToWrite)):
                out_file.write(arrayToWrite[j][2::] + " ")

        print("Success!")

    def BinaryToImage(self):
        print("Converting started...")
        with open(self.path, "rb") as infile:
            try:
                binary = base64.b64encode((infile.read()))
                image = BytesIO(binary)  # <_io.BytesIO object at 0x000001710705D3A0>
                img = Image.open(image)
                x = Image._show(img)


            except Exception:
                print("ERROR!")

        print("Success!")


#if __name__ == "__main__":
#    con = convert("hello")
#
#    con.ImageToBytes()
#    con.BytesToImage()
#    con.ImageToBinary()
#    con.BinaryToImage()
