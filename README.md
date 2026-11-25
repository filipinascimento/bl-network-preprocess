[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.1-blue.svg)](https://doi.org/10.25663/brainlife.app.289)

# Network Preprocess

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Filters a connectivity network by weight sign, threshold and top-percentile edges and outputs the preprocessed network, weighted or binarised.**

Python utility for network analysis. It transforms edge weights by sign (absolute, positive or negative), removes edges under a threshold and/or keeps a top percentile of edges, optionally keeping weights. Use it to sparsify connectivity matrices before computing network measures.

| | |
|---|---|
| 📥 **Inputs** | `generic/network` |
| 📤 **Outputs** | `generic/network` |
| 🐳 **Container** | `filsilva/cxnetwork:0.2.0` |
| ⚙️ **Resources** | 1 CPUs |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.289](https://doi.org/10.25663/brainlife.app.289) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `network` | `generic/network` | yes | Input network files to preprocess. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `output` | `generic/network` | Resulting preprocessed networks. |

<details>
<summary><b>⚙️ Parameters</b> (7)</summary>

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

📚 **References used by this App:**
- Avesani P, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)
- Bassett DS, Sporns O. Network neuroscience. Nat Neurosci 20(3):353 (2017). [doi:10.1038/nn.4502](https://doi.org/10.1038/nn.4502)

<!-- brainlife-app:end -->

App to preprocess networks and generate a filtered version of it, which can be directed or undirected, weighted or unweighted.

### Authors
- [Filipi N. Silva](https://filipinascimento.github.io)

### Contributors
- [Franco Pestilli](https://liberalarts.utexas.edu/psychology/faculty/fp4834)


### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)


### Citations
1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

2. Bassett, Danielle S., and Olaf Sporns. "Network neuroscience." Nature neuroscience 20, no. 3 (2017): 353. [https://doi.org/10.1038/nn.4502](https://doi.org/10.1038/nn.4502)


## Running the App 

### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/brainlife.app.289](https://doi.org/10.25663/brainlife.app.289) via the "Execute" tab.

### Running Locally (on your machine)
Singularity is required to run the package locally.

1. git clone this repo.

```bash
git clone <repository URL>
cd <repository PATH>
```

2. Inside the cloned directory, edit `config-sample.json` with your data or use the provided data.

3. Rename `config-sample.json` to `config.json` .

```bash
mv config-sample.json config.json
```

4. Launch the App by executing `main`

```bash
./main
```

The `filsilva/cxnetwork` ( [https://github.com/filipinascimento/cxnetworks-docker](https://github.com/filipinascimento/cxnetworks-docker) ) docker image is being used.

### Sample Datasets

A sample dataset is provided in folder `data` and `config-sample.json`

## Output

The output is a preprocessed `network` data type.

### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install the python packages defined in `environment.yml`, then you can run the code directly from python using:  

```bash
./main.py config.json
```

