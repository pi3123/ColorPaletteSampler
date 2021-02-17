class conversions:
    @staticmethod
    def rgb_to_hex(r, g, b):
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    @staticmethod
    def rgb_to_cmyk(r, g, b):
        if (r == 0) and (g == 0) and (b == 0):
            # black
            return 0, 0, 0, 100

        # rgb [0,255] -> cmy [0,1]
        c = 1 - r / float(255)
        m = 1 - g / float(255)
        y = 1 - b / float(255)

        # extract out k [0,1]
        min_cmy = min(c, m, y)
        c = (c - min_cmy)
        m = (m - min_cmy)
        y = (y - min_cmy)
        k = min_cmy

        # rescale to the range [0,cmyk_scale]
        return int(c * 100), int(m * 100), int(y * 100), int(k * 100)

    @staticmethod
    def rgb_to_hsv(r, g, b):
        r, g, b = r / 255.0, g / 255.0, b / 255.0
        mx = max(r, g, b)
        mn = min(r, g, b)
        df = mx - mn
        if mx == mn:
            h = 0
        elif mx == r:
            h = (60 * ((g - b) / df) + 360) % 360
        elif mx == g:
            h = (60 * ((b - r) / df) + 120) % 360
        elif mx == b:
            h = (60 * ((r - g) / df) + 240) % 360
        if mx == 0:
            s = 0
        else:
            s = (df / mx) * 100
        v = mx * 100
        return int(h), int(s), int(v)

