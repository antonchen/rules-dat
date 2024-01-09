#!/usr/bin/env python3
import sys
import os

def fix_file(delete_file):
    """修复 rules 中的行，最后一行需要一行空行"""
    with open(delete_file, "r") as f:
        lines = f.readlines()
    with open(delete_file, "w") as f:
        for line in lines:
            if line.strip():
                f.write(line)
        f.write("\n")

def delete_line(rules_file, dest_file):
    """删除 dest_file 中包含 rules_file 中的行"""
    fix_file(rules_file)
    with open(rules_file, "r") as f:
        lines = f.readlines()
    with open(dest_file, "r") as f:
        dest_lines = f.readlines()
    with open(dest_file, "w") as f:
        for line in dest_lines:
            if line not in lines:
                f.write(line)
            else:
                print("Delete line: {} in {}".format(line.strip(), os.path.basename((dest_file))))
def add_line(rules_file, dest_file):
    """添加 rules_file 中的行到 dest_file，添加前检查不包含"""
    fix_file(rules_file)
    with open(rules_file, "r") as f:
        lines = f.readlines()
    with open(dest_file, "r") as f:
        dest_lines = f.readlines()
    with open(dest_file, "a") as f:
        for line in lines:
            if line not in dest_lines:
                f.write(line)
                print("Add line: {} to {}".format(line.strip(), os.path.basename((dest_file))))
            else:
                print("Skip line: {} in {}".format(line.strip(), os.path.basename((dest_file))))

def merge_rules(rules_dir, dest_dir):
    """合并 rules_dir 目录下的所有文件到 dest_dir"""
    for file in os.listdir(rules_dir):
        if file.endswith(".txt"):
            action, _, dest = file.split(".")[0].split("-")
            rules_file = os.path.join(rules_dir, file)
            dest_file = os.path.join(dest_dir, dest)
            if action == "delete":
                delete_line(rules_file, dest_file)
            elif action == "add":
                add_line(rules_file, dest_file)
            else:
                print("Unknown action: {}".format(action))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: {} rules_dir dest_dir".format(sys.argv[0]))
        sys.exit(1)
    rules_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    merge_rules(rules_dir, dest_dir)
