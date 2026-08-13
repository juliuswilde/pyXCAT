# pyXCAT

Python wrapper for the XCAT phantom generator

Used to generate parameter sets for the XCAT generator as pydantic models and to run the generator.

As this is only a wrapper it requires XCAT to run which you can request [here](https://cvit.duke.edu/resource/xcat-phantom-program/) or by contacting [Paul Segars](paul.segars@duke.edu).

## Usage

An example can be found in [main](main.py). Just change the `exe_path` to the path to the actual location of the executable. Keep in mind that there are two different executables for windows and linux.

For the main the paths to the different inputs are assumed to be relative to the XCAT folder. This is how I got the data from Paul.That assumption is done through the `os.chdir(exe_path.parent)`.

When running a parameter file is generated and saved at the output location. For that all paths get converted to absolute from the working directory. So generally paths can be expressed as relative to the working directory but using absolute paths is recommended.

After the example is running just change parameters in the different sections of the `XCATParameters` pydantic model to customize the output.