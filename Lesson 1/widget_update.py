from process import CpuBar
import tkinter
class Configure_widgets:

    def configure_cpu_bar(self):
        r = self.cpu.cpu_percent_return()
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].configure(text=f'core {i+1} usage: {r[i]}%')
            self.list_prbar[i].configure(value=r[i])


        r2 = self.cpu.ram_usage()
        self.ram_lab.configure(text=f'RAM usage : {r2[2]}%, \
                                    \n total : {round(r2[0]/1048576)} Mb\
                                    \n used : {round(r2[3]/1048576)} Mb,\
                                    \n free : {round(r2[4]/1048576)} Mb ')


        self.ram_bar.configure(value=r2[2])


        self.whel = self.after(1000, self.configure_cpu_bar)