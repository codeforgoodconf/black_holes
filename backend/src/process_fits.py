import os
import numpy
from astropy.io import fits
import config


def lerp(a, b, t):
    return (1.0 - t) * a + t * b


def remove_slope(wls, fxs):
    edge_wl = [4517, 4785]

    ew = 50.0
    ewo2 = ew / 2

    edge_sum = [0, 0]
    edge_points = [0, 0]
    for i, edge in enumerate(edge_wl):
        for j, fx in enumerate(fxs):
            if edge - ewo2 < wls[j] < edge + ewo2:
                edge_sum[i] += fx
                edge_points[i] += 1
    edge_ave = [edge_sum[i] / edge_points[i] for i in range(2)]

    slope = (edge_ave[1] - edge_ave[0]) / (edge_wl[1] - edge_wl[0])
    y_int = edge_ave[0] - slope * edge_wl[0]

    for i, wav_val in enumerate(wls):
        fxs[i] -= (slope * wav_val + y_int)


def gaussian_smooth(wav_rest, fwav):
    kernel_width = 2
    stepsize = wav_rest[1] - wav_rest[0]

    num_steps = int(kernel_width / stepsize * 3)  # Calculate out to 1%
    kernel = [numpy.exp(-((i * stepsize) ** 2) / (2 * kernel_width ** 2))
              for i in range(num_steps)]
    kernel = kernel[::-1] + kernel[1:]
    kernel = [i / numpy.sum(kernel) for i in kernel]  # normalize the kernel

    fwav_smooth = [0] * (len(fwav) - len(kernel) + 1)
    wav_rest_smooth = [0] * (len(fwav) - len(kernel) + 1)
    for i in range(len(fwav_smooth)):
        use_fwav_vals = fwav[i:i + len(kernel)]
        fwav_smooth[i] = numpy.sum([use_fwav_vals[j] * kernel[j]
                                    for j in range(len(kernel))])
        wav_rest_smooth[i] = wav_rest[i + int((len(kernel) - 1) / 2)]

    return wav_rest_smooth, fwav_smooth


def crop_data(wls, fxs, wls_out):
    wl_min = wls_out[0]
    wl_max = wls_out[-1]
    wlsc = [wls[i] for i in range(len(wls)) if wl_min < wls[i] < wl_max]
    fxsc = [fxs[i] for i in range(len(wls)) if wl_min < wls[i] < wl_max]
    return wlsc, fxsc


def process_fits(file_path, wls_out):
    print('processing ' + file_path)
    hdulist = fits.open(file_path)
    wls = 10 ** hdulist[1].data['loglam']
    fxs = hdulist[1].data['flux']
    z = hdulist[2].data['z']
    wls = wls / (1 + z)
    if wls_out[0] < wls[0] or wls_out[-1] > wls[-1]:
        return None
    remove_slope(wls, fxs)
    wls, fxs = gaussian_smooth(wls, fxs)
    wls, fxs = crop_data(wls, fxs, wls_out)
    fxs_out = numpy.interp(wls_out, wls, fxs)
    return fxs_out


def process_folder(folder_path, wls_out, label):
    fluxes = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.fits'):
            file_path = os.path.join(folder_path, file_name)
            flux = process_fits(file_path, wls_out)
            if flux is not None:
                flux = list(flux)
                flux.insert(0, label)
                flux.insert(0, os.path.splitext(file_name)[0])
                fluxes.append(flux)
    return fluxes


def save_csv(name, table):
    with open(name, 'w') as file:
        for i in range(len(table)):
            for j in range(len(table[i])):
                file.write(str(table[i][j]))
                if j < len(table[i]) - 1:
                    file.write(',')
            file.write('\n')


def main():
    path_negatives = os.path.join(config.DATA_ROOT, "negatives")  # 'D:\\data\\blackhole_spectra\\negatives'
    path_positives = os.path.join(config.DATA_ROOT, "positives")  # 'D:\\data\\blackhole_spectra\\positives'
    path_output = os.path.join(config.DATA_ROOT, "compiled.csv")  # 'D:\\data\\blackhole_spectra\\compiled.csv'

    wl_min = 4686 - 150
    wl_max = 4686 + 150
    n_samples = 300

    wls_out = [lerp(wl_min, wl_max, i / (n_samples - 1)) for i in range(n_samples)]

    table = []

    header = ['file', 'label']
    header.extend(wls_out)
    table.append(header)

    negatives = process_folder(path_negatives, wls_out, 0)
    positives = process_folder(path_positives, wls_out, 1)

    table.extend(negatives)
    table.extend(positives)

    save_csv(path_output, table)


if __name__ == '__main__':
    main()
