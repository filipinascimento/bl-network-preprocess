<h1 align="center">Network Preprocess</h1>

<p align="center">
  Filters a connectivity network by weight sign, threshold and top-percentile edges and outputs the preprocessed network, weighted or binarised.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.289"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.289-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-see_LICENSE-lightgrey.svg" alt="License"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Filters a connectivity network by weight sign, threshold and top-percentile edges and outputs the preprocessed network, weighted or binarised.**

Python utility for network analysis. It transforms edge weights by sign (absolute, positive or negative), removes edges under a threshold and/or keeps a top percentile of edges, optionally keeping weights. Use it to sparsify connectivity matrices before computing network measures.

| | |
|---|---|
| **Inputs** | `generic/network` |
| **Outputs** | `generic/network` |
| **Container** | `filsilva/cxnetwork:0.2.0` |
| **Resources** | 1 CPUs |
| **Run it** | [doi.org/10.25663/brainlife.app.289](https://doi.org/10.25663/brainlife.app.289) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `network` | `generic/network` | yes | Input network files to preprocess. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `output` | `generic/network` | Resulting preprocessed networks. |

<details>
<summary><b>Parameters</b> (7)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `transform` | enum | `absolute` | Choose how to handle the sign of the weights. Absolute: Uses the absolute value of entries as weights. Positive: Uses only positive weights. Negative: Set all negative weights to positive, and positive to zero weight. Layered: Keep weights unchanged but adds separated layers for negative and positive. None : Makes no changes to the signs of entries. Options: `absolute`, `positive`, `negative`, `layered`, `none`. |
| `retain-weights` | boolean | `false` | Retain weights values after filtering (If not enabled, the resulting networks are unweighed.) |
| `threshold` | number |  | If a value is provided, all edges weighting less than threshold are removed. |
| `percentile` | number |  | Percentile of top edges to be kept in the network after thresholding edges. |
| `selection-transform` | enum | `same` | . Absolute: Uses the absolute value of entries as weights. Positive: Uses only positive weights. Negative: Set all negative weights to positive, and positive to zero weight. None : Makes no changes to the signs of entries. Same: Use same transformation as transform. Options: `absolute`, `positive`, `negative`, `none`, `same`. |
| `strict-percentile` | boolean | `false` | Apply the percentile filter based on the order of weights. |
| `keep-zero-weights` | boolean | `false` | Keep edges with weight zero before threshold and percentile filtering. |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.289](https://doi.org/10.25663/brainlife.app.289), choose `generic/network` from your project, set the parameters and press **Execute**. The results are saved to your project as `generic/network`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `filsilva/cxnetwork:0.2.0`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "network": "/path/to/network/network",
       "transform": "absolute",
       "retain-weights": false,
       "threshold": "<number>",
       "percentile": "",
       "selection-transform": "same",
       "strict-percentile": false,
       "keep-zero-weights": false
   }
   ```

3. Run `./main`.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Network Preprocess. brainlife.io App. [doi:10.25663/brainlife.app.289](https://doi.org/10.25663/brainlife.app.289)
- Bassett DS, Sporns O. Network neuroscience. Nat Neurosci 20(3):353 (2017). [doi:10.1038/nn.4502](https://doi.org/10.1038/nn.4502)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- [Filipi N. Silva](https://filipinascimento.github.io)

**Contributors**

- [Franco Pestilli](https://liberalarts.utexas.edu/psychology/faculty/fp4834)

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>

## License

See [LICENSE](LICENSE).
