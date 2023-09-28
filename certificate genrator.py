
try:
    def print_certificate(n, counter):
        certificate = ""
        with open(r"./assets/sample"+str(counter)+".txt", "w") as fp2:
            for dash in range(85):
                certificate += "-"

            for x in range(16):
                for y in range(85):
                    if y == 0:
                        certificate += "\n|"
                    if x == 0 and y == 24:
                        certificate += "Certificate of Completion"
                        y -= len("Certificate of Completion")
                    if x == 3 and y == 6:
                        certificate += "This is to certify that " + "\""+n + "\"" + " has successfully completed the          |"
                        certificate += "\n" + "|          course in Micro Biology."
                    if (x == 9 and y == 10) or (x == 9 and y == 35):
                        certificate += "___________________"
                    if x == 10 and y == 8:
                        certificate += "Signature of Instructor"
                    if x == 10 and y == 33:
                        certificate += "Signature of HOD"
                    if y == 84:
                        certificate += "|"
                    else:
                        if x == 0 and 24 < y < 50:
                            pass
                        if x == 3 and y <= 72:
                            pass
                        else:
                            certificate += " "
            certificate += "\n"
            for dash in range(85):
                certificate += "-"
            fp2.write(certificate)


    with open(r"./sampleInput.txt", "r") as fp1:
        count = 1
        name_list = fp1.readlines()
        for name in name_list:
            for candidate_name in name.split(","):
                print_certificate(candidate_name, count)
                count += 1

except FileNotFoundError as e:
    print(e)
