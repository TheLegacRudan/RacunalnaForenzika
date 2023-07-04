import os
import pandas as pd
import hashlib
import magic
import mimetypes

dir_path = 'C:\\Users\\A508\\ilegac\\LAB-3\\evid'
md5s = []
sha1s = []
sha256s = []
magic_numbers = []
extensions = []
file_names = []
extension_matches = []
mag_obj = magic.Magic(mime=True)

for file in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, file)):
        (file_name, extension) = os.path.splitext(file)
        file_names.append(file_name)
        extensions.append(extension)

        with open(file, 'rb') as f:
            data = f.read()
            magic_number = mag_obj.from_file(os.path.join(dir_path, file))
            magic_numbers.append(magic_number)
            md5hash = hashlib.md5(data).hexdigest()
            md5s.append(md5hash)
            sha1hash = hashlib.sha1(data).hexdigest()
            sha1s.append(sha1hash)
            sha256hash = hashlib.sha256(data).hexdigest()
            sha256s.append(sha256hash)

            if extension.lower() == '':
                extension_matches.append(False)
            elif mimetypes.guess_type('test'+extension.lower())[0] in magic_number.lower():
                extension_matches.append(True)
            else:
                extension_matches.append(False)

df = pd.DataFrame({'file_name': file_names, 'extension': extensions,
                  'md5': md5s, 'sha1': sha1s, 'sha256': sha256s, 'magic_number': magic_numbers, 'extension_match': extension_matches})
print(df)