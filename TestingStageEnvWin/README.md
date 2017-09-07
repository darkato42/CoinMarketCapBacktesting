# Setting up the env
1.  Use conda to create a new environment
2.  Within the new env, install zipline so you won't have any dependency conflict

```conda create -y -c quantopian zipline=1.1.1 python=2.7 -n zipline-env```

## 7 Sep 2017
Progress so far on setting up Zipline for backtesting.

For zipline to use a digital asset data source, a custom data bundle is required. However, there isn't anyone available right now.
For adding an custom bundle, details are available [here](http://www.prokopyshen.com/create-custom-zipline-data-bundle). The instructions aren't clear about how to register the bundle using extension.py . This extension.py file is under the hidden folder .zipline, check [here](https://www.quantopian.com/posts/zipline-issue-while-creating-custom-bundle-to-bring-yahoo-data) for clarification. 

Another issue I haven't figured out seems to be the calendar. Because bitcoin is traded around the clock 24/7 which is different from other stock exchanges. The default calendar has to be tweaked.
