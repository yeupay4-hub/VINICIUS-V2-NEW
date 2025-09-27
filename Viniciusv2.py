import os, sys, zlib, gzip, lzma, base64, marshal, time, threading, hashlib, random, string, psutil, binascii, codecs
RESET = "\033[0m"

def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def gradient_text(text, colors):
    lines = text.splitlines()
    result = ""
    total_chars = sum(len(line) for line in lines if line.strip())
    idx = 0
    for line in lines:
        for ch in line:
            t = idx / max(total_chars-1, 1)
            seg = int(t * (len(colors)-1))
            c1, c2 = colors[seg], colors[min(seg+1, len(colors)-1)]
            ratio = (t * (len(colors)-1)) - seg
            r = int(c1[0] + (c2[0]-c1[0]) * ratio)
            g = int(c1[1] + (c2[1]-c1[1]) * ratio)
            b = int(c1[2] + (c2[2]-c1[2]) * ratio)
            result += rgb(r,g,b) + ch
            idx += 1
        result += RESET
        if line != lines[-1]:
            result += "\n"
    return result + RESET

def ask(prompt):
    return input(gradient_text(prompt, [(0,255,0), (0,0,255), (255,255,255)]))

banner = r"""
   /$$    /$$ /$$$$$$ /$$   /$$ /$$$$$$  /$$$$$$  /$$$$$$ /$$   /$$  /$$$$$$ 
  | $$   | $$|_  $$_/| $$$ | $$|_  $$_/ /$$__  $$|_  $$_/| $$  | $$ /$$__  $$
  | $$   | $$  | $$  | $$$$| $$  | $$  | $$  \__/  | $$  | $$  | $$| $$  \__/
  |  $$ / $$/  | $$  | $$ $$ $$  | $$  | $$        | $$  | $$  | $$|  $$$$$$ 
   \  $$ $$/   | $$  | $$  $$$$  | $$  | $$        | $$  | $$  | $$ \____  $$
    \  $$$/    | $$  | $$\  $$$  | $$  | $$    $$  | $$  | $$  | $$ /$$  \ $$
     \  $/    /$$$$$$| $$ \  $$ /$$$$$$|  $$$$$$/ /$$$$$$|  $$$$$$/|  $$$$$$/
      \_/    |______/|__/  \__/|______/ \______/ |______/ \______/  \______/

                           VINICIUS VERSION 2.0
                     COPYRIGHT BY NGUYEN NHAT NAM ANH
                           HIGH SPEED OBFUSCATOR
                        ADVANCED VINICIUS OBFUSCATOR

                   __VINICIUS__
                  Obfuscator: Vinicius 
                  Admin: Nguyen Nhat Nam Anh 
                  Banner: VINICIUS 
                  Telegram: https://t.me/ctevclwar 
                  Facebook: https://www.facebook.com/ng.xau.k25
"""

colors = [(0,255,0), (0,0,255), (255,255,255)]
print(gradient_text(banner, colors))

def reset_screen():
    os.system("cls" if "Windows" in __import__("platform").uname() else "clear")

if sys.version_info[0] == 2:
    _input = "raw_input('%s')"
elif sys.version_info[0] == 3:
    _input = "input('%s')"
else:
    sys.exit("[+][-] Phiên bản Python không được hỗ trợ!")

def time_check():
    start = time.time()
    for _ in range(1000):
        pass
    if time.time() - start > 0.1:
        sys.exit("[+][-] Obfuscator!")

def trace_check():
    if sys.gettrace():
        sys.exit("[+][-] Anti Crack!")

def process_check():
    debug_tools = ["ollydbg", "ida", "x64dbg", "gdb", "windbg"]
    for proc in psutil.process_iter():
        if any(tool in proc.name().lower() for tool in debug_tools):
            sys.exit("[+][-] Encode!")

def integrity_check():
    with open(__file__, 'rb') as f:
        code = f.read()
    expected_hash = hashlib.sha256(code).hexdigest()
    if expected_hash != hashlib.sha256(code).hexdigest():
        sys.exit("[+][-] Anti Debug!")

def junk_code():
    return ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(50, 100)))

cmp_z = lambda x: zlib.compress(x)
enc_b = lambda x: base64.b64encode(x)
cmp_g = lambda x: gzip.compress(x)
cmp_l = lambda x: lzma.compress(x)
ser_m = lambda x: marshal.dumps(compile(x, '<x>', 'exec'))

def SizeCalc(path):
    if os.path.isfile(path):
        size = os.stat(path).st_size
        for unit in ['Byte', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
    return "0 Byte"

def apply_extra_layers(payload: bytes):
    steps = [
        ("b85", "__import__('base64').a85encode(x)", "__import__('base64').a85decode(x)")
    ]

    extras = [
        ("rev", "x[::-1]", "x[::-1]"),
        ("rot13",
            "__import__('codecs').encode(x.decode(), 'rot_13').encode()",
            "__import__('codecs').decode(x.decode(), 'rot_13').encode()")
    ]

    import random
    if random.choice([True, False]):
        steps.append(random.choice(extras))

    x = payload
    for name, enc_code, dec_code in steps:
        enc_func = eval("lambda x: " + enc_code)
        x = enc_func(x)

    dec_steps = [(name, dec_code) for (name, enc_code, dec_code) in steps]
    return x, dec_steps

def Scramble(data, outfile, use_anticrack):
    process = "enc_b(cmp_z(cmp_l(cmp_g(ser_m(data.encode('utf8'))))))[::-1]"

    assignments = (
        "_NAME_ = " + repr("}__VINICIUS__{") + "\n"
        "_OBF_ = " + repr("Obfuscator: Vinicius") + "\n"
        "_ADMIN_ = " + repr("Obfuscator Owner: Nguyen Nhat Nam Anh") + "\n"
        "_CONTACT_ = " + repr("Telegram: https://t.me/ctevclwar") + "\n"
        "_INFO_ = " + repr("Facebook: https://www.facebook.com/ng.xau.k25") + "\n"
    )

    concat_for_hash = ''.join([
        '}__VINICIUS__{',
        'Obfuscator: Vinicius',
        'Obfuscator Owner: Nguyen Nhat Nam Anh',
        'Telegram: https://t.me/ctevclwar',
        'Facebook: https://www.facebook.com/ng.xau.k25'
    ])
    expected_hash = __import__('hashlib').sha256(concat_for_hash.encode()).hexdigest()

    check_block = (
        "__ctevcl_ = ''.join([_NAME_,_OBF_,_ADMIN_,_CONTACT_,_INFO_])\n"
        "if __import__('hashlib').sha256(__ctevcl_.encode()).hexdigest() != " + repr(expected_hash) + ":\n"
        "    raise SystemExit\n"
    )

    try_block = (
        "try:\n"
        "    _Vinicius_ = None"
        "\n"
        "except Exception:\n"
        "    raise SystemExit\n"
    )

    _loading_src = "print('>> Loading...')\n__import__('time').sleep(0.5)\n"
    _loading_m = marshal.dumps(compile(_loading_src, '<x>', 'exec'))
    _loading_b64 = base64.b64encode(_loading_m).decode()
    preamble = "_Vinicius_ = " + repr(_loading_b64) + "\n" \
             + "exec(__import__('marshal').loads(__import__('base64').b64decode(_Vinicius_)))\n"

    decoder_lambda = "_ = lambda __: __import__('marshal').loads(__import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])))))\n"

    prefix = assignments + check_block + try_block + preamble + decoder_lambda

    if use_anticrack:
        noise = base64.b64encode(junk_code().encode()).decode()
        prefix += "_eval_ = " + repr(noise) + "\n"

    try:
        rounds_local = int(rounds)
    except Exception:
        rounds_local = 3
    if rounds_local > 250:
        rounds_local = 250

    try:
        for i in range(rounds_local, 0, -1):
            percent = int((i / max(rounds_local, 1)) * 100)
            try:
                prog = f">> Encoding {(i / max(rounds_local, 1)) * 100:.5f}%... "
                sys.stdout.write("\r" + gradient_text(prog, colors))
                sys.stdout.flush()
            except Exception:
                pass

            try:
                payload = eval(process)
            except Exception as e:
                sys.stdout.write("\n")
                sys.stdout.flush()
                raise RuntimeError("Encoding failed: " + str(e))

            try:
                payload_with_extras, dec_steps = apply_extra_layers(payload)
            except Exception as e:
                payload_with_extras, dec_steps = payload, []

            extra_decode = "x = __\n"
            for name, dec_code in reversed(dec_steps):
                extra_decode += f"x = {dec_code}\n"
            extra_decode += "exec(_(x))\n"

            data = f"globals_ = {repr(payload_with_extras)}\n__ = globals_\n{extra_decode}"

        try:
            sys.stdout.write("\n")
            sys.stdout.flush()
        except Exception:
            pass

    except KeyboardInterrupt:
        sys.stdout.write("\n[!] Bị hủy bởi người dùng\n")
        sys.stdout.flush()
        raise

    try:
        with open(outfile, 'w', encoding='utf-8') as f:
            f.write(prefix + data)
    except Exception as e:
        raise RuntimeError("Không thể ghi file output: " + str(e))

def StartFlow():
    global rounds
    try:
        reset_screen()
        print(gradient_text(banner, colors))

        try:
            print(gradient_text("[...] FILE NAME:", colors), end=" ")
            infile = input()
            try:
                with open(infile, "r", encoding="utf-8") as f:
                    data = f.read()
            except UnicodeDecodeError:
                with open(infile, "rb") as f:
                    data = f.read().decode("utf-8", errors="ignore")
        except IOError:
            sys.exit("[+][-] Tệp không tồn tại!")
        
        rounds = 13

        print(gradient_text("[...] ANTI-DEBUG? (y/n):", colors), end=" ")
        antidebug = input().strip().lower()
        use_antidebug = antidebug == 'y'
        
        print(gradient_text("[...] ANTI-CRACK? (y/n):", colors), end=" ")
        anticrack = input().strip().lower()
        use_anticrack = anticrack == 'y'
        
        if use_antidebug:
            time_check()
            trace_check()
            process_check()
            integrity_check()
        
        if use_anticrack:
            integrity_check()
        
        base = os.path.basename(infile)
        name_only = base.lower().replace('.py', '')
        outdir = os.path.dirname(infile) or '.'
        outname = f"vinicius_{name_only}.py"
        outfile = os.path.join(outdir, outname)
        idx = 1
        while os.path.exists(outfile):
            outfile = os.path.join(outdir, f"vinicius_{name_only}_{idx}.py")
            idx += 1
        
        Scramble(data, outfile, use_anticrack)
        print(gradient_text("[=>] ✅ENCRYPTION SUCCESS %s" % infile, colors))
        print(gradient_text("[=>] SAVE AS %s" % outfile, colors))
        print(gradient_text("[=>] FILE SIZE: %s" % SizeCalc(outfile), colors))
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()

if __name__ == "__main__":
    StartFlow()
