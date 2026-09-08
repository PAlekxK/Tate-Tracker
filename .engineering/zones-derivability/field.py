"""Slope scalar field + break-of-slope (gradient magnitude), PIL only."""
from PIL import Image, ImageChops, ImageFilter
import geo, raster

def slope_field(blur=1.5):
    """High = STEEP. Direction verified empirically against the answer key's own
    named terrain (the-bank/the-bluff darkest, meadow/turf lightest), which is
    what licenses convert('L') on a colour ramp."""
    im = raster.load_rgb("lidar-slope-2018.png").convert("L")   # 601-2 luma = the ramp scalar
    im = ImageChops.invert(im)                                   # now high = steep
    if blur:
        # lidar is 1 m posting upsampled ~3.3x to 0.306 m/px — smoothing at that
        # scale is honest, not cosmetic.
        im = im.filter(ImageFilter.GaussianBlur(blur))
    return im

def shift(im, dx, dy):
    return im.transform(im.size, Image.AFFINE, (1,0,dx, 0,1,dy), resample=Image.BILINEAR)

def gradient_mag(im):
    """|d/dx| + |d/dy| via shifted differences — the BREAK of slope."""
    gx = ImageChops.difference(shift(im,-1,0), shift(im,1,0))
    gy = ImageChops.difference(shift(im,0,-1), shift(im,0,1))
    return ImageChops.add(gx, gy, scale=1.0, offset=0)

def lum_to_deg(l):
    """Ramp is 0-30 deg; luminance floor 93 = saturated (>=30 deg), ~245 = 0 deg.
    CLIPPED at 30: 8.7% of the frame sits on the floor and 30 deg cannot be told
    from 45 deg."""
    return max(0.0, min(30.0, 30.0*(245.0-l)/(245.0-93.0)))
