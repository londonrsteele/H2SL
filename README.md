# Helldivers II Stats Logger

An app created by LR Steele

## Installation


## Quick Start




# Components
## Python Files
### File Tree
`main.py`: Main file containing PyQt app  
`main_window.py`: Parent QtMainWindow widget  
`MyWidgets/`  
├── `Welcome_widget.py`: Widget that serves as landing page of PyQt app  
├── `Log_data_widget.py`: Widget where you choose which type of data to log  
├── `EOM_input_widget.py`: Widget where you input end of mission data  
├── `CAR_input_widget.py`: Widget where you input career logs  
├── `Load_data_widget.py`: Widget where you load save files and can access dashboards  
`browser_mw.py`: Widget that serves as a web browser to view the appropriate local port for each dashboard  
`dashapp.py`: Plotly Dash app for "mixed" career and end of mission data  
`EOM_dashapp.py`: Plotly Dash app for end of mission data  
`CAR_dashapp.py`: Plotly Dash app for career data   
`graphing/`:  
├── `metadata.py`: File with helpful lists and color schemes  
├── `stat_scraper.py`: Tool that "scrapes" data from save files  
├── `accuracy.py`: File with constructor for accuracy chart  
├── `dotplot.py`: File with constructor for dotplot chart  
├── `kill.py`: File with constructor for kills chart  
├── `linegraph.py`: File with constructor for linegraph chart  
├── `missions.py`: File with constructor for missions chart    
├── `stratagems.py`: File with constructor for stratagems chart  
├── `survivor.py`: File with constructor for survivor chart  
`assets/`:  
├── `dashapp_styles.css`: Plotly Dash apps styles  
├── `SAVE_PATH.py`: File to save "save_path" for accessing save files  
├── `stylesheets.py`: Button styles, etc.  
├── `left.png`: png for "back" button   
`save_files/`: default save file directory


### Roadmap
[Miro Link to Roadmap](https://miro.com/app/board/uXjVKqy2cQ8=/)



## Icons
<a href="https://www.flaticon.com/free-icons/ui" title="ui icons">Ui icons created by Freepik - Flaticon</a>


## Versions
PySide - 6.7.2  (Aug 01, 2024)  
QtCore - 6.7.2  (Aug 01, 2024)  
Plotly - 5.23.0 (Aug 06, 2024)  
Dash   - 2.17.1 (Aug 06, 2024)  
Dash DAQ - 0.5.0 (Aug 15, 2024)

## License
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007