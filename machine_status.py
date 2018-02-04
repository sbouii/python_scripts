import socket
import os, sys
import subprocess
import psutil
import argparse
import psutil
def get_hostname(output_dict):
  output_dict["hostname"] = socket.gethostname()
 
def get_ip_address(output_dict):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(('INSERT SOME TARGET WEBSITE.com', 'ANY PORT'))
  s.connect(("8.8.8.8", 80))
  output_dict["ip_address"] = s.getsockname()[0]

def get_memory_usage(output_dict):
#retreive ram details
  ram_dict = {}
  memory_usage = psutil.virtual_memory()
  memory_total_gb = float(memory_usage.total)/(1024*1024*1024)
  memory_used_gb = float(memory_usage.used) / (1024*1024*1024)
  memory_available_gb = float(memory_usage.available)/ (1024*1024*1024)
  memory_buffers_gb = float(memory_usage.buffers) / (1024*1024*1024)
  memory_percent = memory_usage.percent
  ram_dict["memory_total_gb"] = memory_total_gb
  ram_dict["memory_used_gb"] = memory_used_gb
  ram_dict["memory_available_gb"] = memory_available_gb
  ram_dict["memory_buffers_gb"] = memory_buffers_gb
  ram_dict["memory_percent"] = memory_percent
  output_dict["ram"] = ram_dict
# retreive swap details
  swap_dict = {}
  swap_usage = psutil.swap_memory()
  swap_total_gb = float(swap_usage.total)/(1024*1024*1024)
  swap_used_gb = float(swap_usage.used)/(1024*1024*1024)
  swap_free_gb = float(swap_usage.free)/(1024*1024*1024)
  swap_dict["swap_total_gb"] = swap_total_gb
  swap_dict["swap_used_gb"] = swap_used_gb
  swap_dict["swap_free_gb"] = swap_free_gb
  output_dict["swap"] = swap_dict
  
def get_cpu_usage(output_dict):
  output_dict["cpu_count"] = psutil.cpu_count()
  output_dict["cpu_percent"] = psutil.cpu_percent()

def get_disk_usage(output_dict):
  i = 0
  partitions = psutil.disk_partitions()
  for part in partitions:
    part_dict = {}
    part_dict["device"] = part.device
    part_dict["mountpoint"] = part.mountpoint
    part_dict["fs_type"] = part.fstype
    usage = psutil.disk_usage(part.mountpoint)
    part_dict["part_total_gb"] = float(usage.total)/(1024*1024*1024)     
    part_dict["part_used_gb"] = float(usage.used) / (1024*1024*1024)    
    part_dict["part_free_gb"] = float(usage.free) /(1024*1024*1024)
    output_dict["partition_%d"%i] = part_dict
    i = i + 1
def main():
 output_dict = {}
 get_hostname(output_dict)
 get_ip_address(output_dict)
 get_memory_usage(output_dict)
 get_cpu_usage(output_dict)
 get_disk_usage(output_dict)
 for key,val in output_dict.items():
    print key, "=>", val
if __name__ == "__main__":
 main()
