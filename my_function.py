import re

def check_dir_name(dir_name):
# Возвращает True, если название недопустимо
#    if re.fullmatch(r'(?i)con|prn|aux|nul|com1|com2|com3|com4|com5|com6|com7|com8|com9|lpt1|lpt2|lpt3|lpt4|lpt5|lpt6|lpt7|lpt8|lpt9|.*[\?:\\\|/\*><"]+.*', dir_name):
    if re.fullmatch(r'(?i)con|prn|aux|nul|com1|com2|com3|com4|com5|com6|com7|com8|com9|lpt1|lpt2|lpt3|lpt4|lpt5|lpt6|lpt7|lpt8|lpt9|.*[ ?:\|/*><"]+.*', dir_name):

        return True

