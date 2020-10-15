[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.1-blue.svg)](https://doi.org/10.25663/brainlife.app.289)

# Network Preprocess
App to preprocess networks and generate a filtered version of it, which can be directed or undirected, weighted or unweighted.

### Authors
- [Filipi N. Silva](https://filipinascimento.github.io)

### Contributors
- [Franco Pestilli](https://liberalarts.utexas.edu/psychology/faculty/fp4834)


### Funding
[![NIH-1R01EB029272-01](https://img.shields.io/badge/NIH-1R01EB029272_01-blue.svg)](https://projectreporter.nih.gov/project_info_description.cfm?aid=9916138&icde=52173380&ddparam=&ddvalue=&ddsub=&cr=1&csb=default&cs=ASC&pball=)

### Citations

1. Bassett, Danielle S., and Olaf Sporns. "Network neuroscience." Nature neuroscience 20, no. 3 (2017): 353. [https://doi.org/10.1038/nn.4502](https://doi.org/10.1038/nn.4502)


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

