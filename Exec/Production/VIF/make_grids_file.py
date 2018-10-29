#!/usr/bin/env python3
#
# This file creates a grids file for the VIF case
#

# ========================================================================
#
# Imports
#
# ========================================================================
import argparse
import numpy as np


# ========================================================================
#
# Main
#
# ========================================================================
if __name__ == "__main__":

    # ========================================================================
    # Setup

    # Parse arguments
    parser = argparse.ArgumentParser(description="Make grids")
    parser.add_argument("--L", help="Ratio of Ly to Lx", type=int, default=10)
    parser.add_argument(
        "--nyc", help="Number of cells on coarse level (y)", type=int, default=64
    )
    parser.add_argument("--xs", help="Start of fine zone", type=int, default=0)
    parser.add_argument("--xe", help="End of fine zone", type=int, default=12)
    args = parser.parse_args()

    # number of cells on the coarse level
    nxc = args.nyc * args.L

    # Start and end in x direction of fine zone
    Lxs = int(args.xs * args.nyc / 2)
    Lxe = int(args.xe * args.nyc / 2)

    # Grid refinement ratio
    ratio = 2

    # number of levels (only 1 is supported right now)
    nlvls = 1

    # max grid size on each level
    max_grid_size = min(args.nyc / 2, 64)

    # output file name
    oname = "grids_file_{0:d}".format(args.nyc)

    # ========================================================================
    # Write output file
    with open(oname, "w") as of:
        of.write(str(nlvls) + "\n")

        xs = np.arange(Lxs, Lxe, int(max_grid_size))
        xe = xs + int(max_grid_size) - 1

        ys = np.arange(0, int(args.nyc), int(max_grid_size))

        ye = ys + int(max_grid_size) - 1

        XS = np.meshgrid(xs, ys)
        XE = np.meshgrid(xe, ye)
        of.write("{0:d}\n".format(len(XS[0].flatten())))

        for xs, ys, xe, ye in zip(
            XS[0].flatten(), XS[1].flatten(), XE[0].flatten(), XE[1].flatten()
        ):
            of.write("(({0:d},{1:d})({2:d},{3:d}))\n".format(xs, ys, xe, ye))

        # need a blank line at the end of the grids file
        of.write("\n")
