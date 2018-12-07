from kuangjia.report.tes_套件 import External_Member
from kuangjia.data.read_data import Read_Shuju
if __name__=='__main__':
    run=External_Member().generate_report()
    te=Read_Shuju().wenjian()

    print(te)
    # if 'all' in te:
    #     run('tes.*')
    # else:


