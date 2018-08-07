from xlrd import open_workbook


class Interface(object):
    def __init__(self, old_int, new_int, neg, bd, dot1q, descrip, mtu,
     vrf, xc_peer, xc_vcid, qos_in, qos_out, ip1, ip2, ip3, ip4):
        self.old_int = old_int
        self.new_int = new_int
        self.neg = neg
        self.bd = bd
        self.dot1q = dot1q
        self.descrip = descrip
        self.mtu = mtu
        self.vrf = vrf
        self.xc_peer = xc_peer
        self.xc_vcid = xc_vcid
        self.qos_in = qos_in
        self.qos_out = qos_out
        self.ip1 = ip1
        self.ip2 = ip2
        self.ip3 = ip3
        self.ip4 = ip4

    def __str__(self):
        return("  old_int: {0}\n"
               "  new_int: {1}\n"
               "  neg: {2}\n"
               "  bd: {3}\n"
               "  dot1q: {4}\n"
               "  descrip: {5}\n"
               "  mtu: {6}\n"
               "  vrf: {7}\n"
               "  xc_peer: {8}\n"
               "  xc_vcid: {9}\n"
               "  qos_in: {10}\n"
               "  qos_out: {11}\n"
               "  ip1: {12}\n"
               "  ip2: {13}\n"
               "  ip3: {14}\n"
               "  ip4: {15}\n"
               .format(self.old_int, self.new_int, self.neg, self.bd, self.dot1q,
               self.descrip, self.mtu, self.vrf, self.xc_peer, self.xc_vcid, self.qos_in, self.qos_out,
               self.ip1, self.ip2, self.ip3, self.ip4))

# Load in the workbook
wb = open_workbook('UIOCNDE01_test.xlsx')
sheet_names = wb.sheet_names()
sheet = wb.sheet_by_name(sheet_names[0])

number_of_rows =  sheet.nrows
number_of_columns = sheet.ncols 

items = []

for row in range(1, number_of_rows):
    values = []
    for col in range(number_of_columns):
        value = (sheet.cell(row,col).value)
        try:
            value = str(int(value))
        except ValueError:
            pass
        finally:
            values.append(value)
    item = Interface(*values)
    items.append(item)

file = open('prov-service-model/deploy-model.yml', 'a+')
file.write('---\n')
file.write('interfaces:\n')
for item in items:
    file.write('-\n')
    file.write(str(item))

file.close()