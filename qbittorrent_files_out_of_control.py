# 查找文件夹内脱离 qBittorrent 管理的文件
#
# 文档
# https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)

import requests
import os
import urllib.parse as urlparse

QB_API_BASE = "http://127.0.0.1:8080/api/v2/"
TARGET_DIR = ""


def get_torrent_list():
    api = urlparse.urljoin(QB_API_BASE, "torrents/info")
    resp = requests.get(api)
    return resp.json()


def get_torrent_contents(hash_):
    api = urlparse.urljoin(QB_API_BASE, "torrents/files")
    resp = requests.get(api, params={"hash": hash_})
    return resp.json()


def get_all_qbittorrent_files():
    torrent_list = get_torrent_list()
    file_list = []
    for torrent in torrent_list:
        contents = get_torrent_contents(torrent["hash"])
        for con in contents:
            path = os.path.join(torrent["save_path"], con["name"])
            file_list.append(path)
    return file_list


def main():
    qb_file_list = get_all_qbittorrent_files()
    for i in range(len(qb_file_list)):
        path = qb_file_list[i]
        qb_file_list.append(path + ".!qB")
    qb_file_set = set(map(os.path.abspath, qb_file_list))

    dir_file_list = []
    for root, subdirs, files in os.walk(TARGET_DIR):
        for f in files:
            dir_file_list.append(os.path.join(root, f))
    dir_file_set = set(map(os.path.abspath, dir_file_list))

    ooc = sorted(list(dir_file_set - qb_file_set))
    for p in ooc:
        print(p)


if __name__ == "__main__":
    main()
