# #from sshtunnel import SSHTunnelForwarder
# import paramiko
#
# dot = ':'
#
# server = "10.247.128.51"
# ssh_username = "root"
# ssh_password="1q2w3e"
#
# ssh = paramiko.SSHClient()
#
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#
# ssh.connect(server, port=22, username=ssh_username, password=ssh_password)
# ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('vzlist -o "ctid,ip,hostname"')
# output = ssh_stdout.readlines()
#
# temp = ""
#
# list_of_containers = []
# for i in output:
#     p = i.split(' ')
#     for k in p:
#         if k == '' or k.startswith('CTID') or k.startswith('HOST') or k.startswith('IP'):
#             pass
#         elif k.endswith('\n'): #  len(k) > 1 and k[-2:0] is '\n':
#             temp += k[0: (len(k)-1)]
#             list_of_containers.append(temp)
#             temp = ""
#         else:
#             temp += '{}{}'.format(k, dot)
#
# print(list_of_containers)
#
# comp_o_365 = 'o365-agent-'
# comp_g_suite = 'gsuite-agent-'
# comp_arch_browse = 'c2c-archive-browsing-service-'
#
# def find_build(ctid, item):
#     pass
#
#
# ssh.close()


g_st = 'gsuite'
o_365 = 'o365'
arch_b = 'archbrowse'

l_s = ['gsuite', 'o365', 'archbrowse']

list_of_param = ['20003:10.247.128.62:c2cabc77-accountsrv-20003.acronis', '20004:10.247.128.63:c2cabc77-datacontrol-20004.acronis', '20005:10.247.128.100:c2cabc77-postie-20005.acronis', '20006:10.247.128.101:c2cabc77-statssrv-20006.acronis', '20016:10.247.128.64:c2cabc77-asc-20016.acronis', '20017:10.247.128.65:c2cabc77-crs-20017.acronis', '20020:10.247.128.66:c2cabc77-rs-20020.acronis', '20030:10.247.128.67:c2cabc77-ams-20030.acronis', '20040:10.247.128.68:c2cabc77-wcs-20040.acronis', '20050:10.247.128.69:c2cabc77-boris-20050.acronis', '20059:10.247.128.80:c2cabc77-fw-20059.acronis', '20066:10.247.128.98:c2cabc77-mysqlproxy-20066.acronis', '20075:10.247.128.99:c2cabc77-reporting-20075.acronis', '20080:10.247.128.81:c2cabc77-amqp-20080.acronis', '20081:10.247.128.82:c2cabc77-amqp-20081.acronis', '20085:10.247.128.83:c2cabc77-mysql-20085.acronis', '20090:10.247.128.84:c2cabc77-graphite-20090.acronis', '20092:10.247.128.85:c2cabc77-consul-20092.acronis', '20093:10.247.128.86:c2cabc77-consul-20093.acronis', '20094:10.247.128.87:c2cabc77-consul-20094.acronis', '20095:10.247.128.88:c2cabc77-fes-20095.acronis', '20100:10.247.128.89:c2cabc77-bckp_nsq-20100.acronis', '20130:10.247.128.90:c2cabc77-appaccountsrv-20130.acronis', '20140:10.247.128.95:c2cabc77-apigw-20140.acronis', '20150:10.247.128.96:c2cabc77-taskmanager-20150.acronis', '20160:10.247.128.97:c2cabc77-provisionmgr-20160.acronis', '20190:10.247.128.102:c2cabc77-bckp_sched-20190.acronis', '20200:10.247.128.103:c2cabc77-bckp_vmgr-20200.acronis', '20400:10.247.128.104:c2cabc77-bckp_c2cmgr-20400.acronis', '20410:10.247.128.105:c2cabc77-bckp_archbrowse-20410.acronis', '20420:10.247.128.106:c2cabc77-bckp_archmgmt-20420.acronis', '20430:10.247.128.53:c2cabc77-bckp_o365agent-20430.acronis', '20440:10.247.128.108:c2cabc77-bckp_amgr-20440.acronis', '20450:10.247.128.54:c2cabc77-bckp_gsuiteagent-20450.acronis', '20500:10.247.128.52:c2cabc77-elk-20500.acronis']



# find uid, ip, hostname for needed conteiner where param is the output of vzlist command
def find_target(param, list_of_prmt):
    for item in list_of_prmt:
        for i in range (0, len(item)):
            if item[i] == param[0] and item[i:(i+len(param))] == param:
                return item


def get_uid(item):
    # split str to 3 items in list - uid, ip, hostname
    k = item.split(':')
    #print('DEBUG: get_uid function output ', k)
    return k[0]


def enter_to_conteiner_cmd(uid):
    enter_command = 'vzctl enter {}'.format(uid)

    return enter_command

def get_version_cmd(what_find):
    command = 'rpm -qa | grep {}'.format(what_find)

    return command

def exit_cmd():
    command = 'exit'

    return command

def run_command(command, need_output = False):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    if need_output == True:
        output = ssh_stdout.readlines()
        return output
    else:
        pass

def main():


    print("Start")
    lst_of_versions = dict()
    # structure 'gsuite', 'o_365', 'archbrowse']
    ls_of_needed_containers = []
    find_and_save_to_list(l_s, list_of_param, ls_of_needed_containers)

    ls_of_uids = []
    #print('DEBUG: list of needed containers ', ls_of_needed_containers)
    for i in ls_of_needed_containers:
        #print("i = ", i)
        uid = get_uid(i)
        ls_of_uids.append(uid)
        #print('DEBUG: list of uids ', ls_of_uids)

    for i in ls_of_uids:
        run_command(enter_to_conteiner_cmd(i))

        version = run_command(get_version_cmd(i), need_output=True)
        lst_of_versions['{}'.format(i)] = version
        run_command(exit_cmd())

    print(lst_of_versions.items())
    print('Finished')





def find_and_save_to_list(what_to_fined, where_fined, where_save):

    for find_item in what_to_fined:
        #print ('DEBUG: what to fined: ', what_to_fined)
        needed_item = find_target(find_item, where_fined)
        #print('DEBUG: fined item ', find_item, '\n', 'DEBUG: where fined: ', where_fined)
        #print('DEBUG: needed item ', needed_item)
        where_save.append(needed_item)
        #print('DEBUG: where save ', where_save)

    return where_save


main()