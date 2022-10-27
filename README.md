<div id="top"></div>

<!-- Title -->
# iTrust SWaT Historian OPC Client

<!-- Description -->
## Description
SWaT Testbed Historian OPC Client is meant to extract real time data of the plant using OPCUA.

### Requirements
* Python >= 3.7
<p align="right">(<a href="#top">back to top</a>)</p>

### Installation
* With pip
   ```
   pip install -r requirements.txt
   ```
<p align="right">(<a href="#top">back to top</a>)</p>

## Usage
* Data is stored in line 23, variable 'data'. You can filter the values by indicating the tag name.
   ```
   print(data["Timestamp"], data["FIT101.Pv"], data["LIT101.Pv"])
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the GNU License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

iTrust - itrust@sutd.edu.sg

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [Francisco Furtado](ifyouaretea@gmail.com)

<p align="right">(<a href="#top">back to top</a>)</p>