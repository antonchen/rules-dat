#!/usr/bin/env python3
import sys

def fix_delete_file(delete_file):
    """修复 delete_file 中的行，最后一行需要一行空行"""
    with open(delete_file, "r") as f:
        lines = f.readlines()
    with open(delete_file, "w") as f:
        for line in lines:
            if line.strip():
                f.write(line)
        f.write("\n")

def delete_line(delete_file, dest_file):
    """删除 dest_file 中包含 delete_file 中的行"""
    fix_delete_file(delete_file)
    with open(delete_file, "r") as f:
        lines = f.readlines()
    with open(dest_file, "r") as f:
        dest_lines = f.readlines()
    with open(dest_file, "w") as f:
        for line in dest_lines:
            if line not in lines:
                f.write(line)
            else:
                print("Delete line: {}".format(line.strip()))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: {} delete_file dest_file".format(sys.argv[0]))
        sys.exit(1)
    delete_file = sys.argv[1]
    dest_file = sys.argv[2]
    delete_line(delete_file, dest_file)
