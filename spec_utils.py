def wavelengths_itr():
    wvs = []
    spec = 400
    while spec <= 2499.5:
        n_spec = spec
        if int(n_spec) == spec:
            n_spec = int(n_spec)
        wavelength = str(n_spec)
        yield wavelength
        spec = spec + 0.5
    return wvs


def get_wavelengths():
    return ["B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08", "B8A", "B09", "B11", "B12"]


def get_wavelengths_str():
    return ",".join(get_wavelengths())


def get_rgb():
    return ["B02", "B03", "B04"]