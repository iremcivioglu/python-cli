import os
from os import listdir, path
from os.path import isfile, join
import shutil
import argparse


def classify_files(args):
    args.current_directory = input("Dizin: ")
    os.chdir(args.current_directory)

    args.file_list = [file for file in listdir(args.current_directory) if
                      isfile(join(args.current_directory, file))]  # kullanıcının girdiği dizindeki dosyaları listeler
    args.ext = []

    for i in args.file_list:
        extentions = os.path.splitext(i)[1][1:]  # dosya ve klasörlerin uzantılarını dot('.') olmadan ayırır
        args.ext.append(extentions)  # oluşturulan ext listesine, uzantılar ekleniyor
        # print("Ext:", extentions)

    for j in range(len(args.ext)):
        if os.path.exists(args.ext[j]):
            continue
        else:
            os.mkdir(str(args.ext[j]))  # uzantı isimleri ile klasörler oluşturuluyor

        for file_name in args.file_list:
            new_dir = os.path.join(args.current_directory, args.ext[j])  # uzantı adı ile oluşturulan klasörleri, mevcut dizine ekleyip yeni bir dizin oluşturuluyor
            if file_name.endswith(args.ext[j]):
                shutil.move(file_name, str(new_dir))  # dosyalar, uzantı isimleri ile oluşturulan klasörlere taşındı
    print("Dosyalar ilgili klasörlere taşındı.")


def main():
    parser = argparse.ArgumentParser() 
    parser.add_argument('--classify', help='Dosyaları uzantılarına göre sınıflandırmak için komutu giriniz.')
    parser.set_defaults(func=classify_files)
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
