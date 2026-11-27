"""ห่อไฟล์ HTML แบบ artifact (ไม่มี <head>) ให้เป็นหน้าเว็บเต็ม
ใช้: python3 tools/wrap.py <ไฟล์ต้นทาง.html> <ไฟล์ปลายทาง.html>"""
import sys
src,dst=sys.argv[1],sys.argv[2]
h=open(src,encoding='utf-8').read()
if h.lstrip().lower().startswith('<!doctype'):
    open(dst,'w',encoding='utf-8').write(h); sys.exit()
HEAD='<!doctype html>\n<html lang="th">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 32 32%22%3E%3Crect width=%2232%22 height=%2232%22 rx=%228%22 fill=%22%23f02585%22/%3E%3Ctext x=%2216%22 y=%2222%22 font-size=%2216%22 text-anchor=%22middle%22 fill=%22white%22 font-family=%22sans-serif%22%3ER8%3C/text%3E%3C/svg%3E">\n<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}</style>\n'
h=h.replace('https://claude.ai/artifact/GPddXCkEgPgMmtzLosXeH1','/check/').replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
i=h.find('</style>')+len('</style>')
open(dst,'w',encoding='utf-8').write(HEAD+h[:i]+'\n</head>\n<body>\n'+h[i:]+'\n</body>\n</html>\n')
