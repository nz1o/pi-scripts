To create a new Alexa Skill, log in to the Alexa Developer Console at https://developer.amazon.com/alexa/console/ask with your Amazon account.  Keep in mind that because you are working in a developer environment **this Skill will only be available to Alexa devices associated with the same Amazon account as you used to log in to the developer console**.

Here are screenshots of the important configuration areas for your Alexa Skill.  Some of these values can be changed while others must remain the same to work with the accompanying script.  I will attempt to call out which values can be changed and which cannot as we look at each page.  

### Creating the Skill 

To create a new Skill click **Create Skill** fromt the main Developer Console page.  You may give your Skill any name you wish.  Choose the **Custom** model and select the **Provision your own** backend method.  When asked to select a template, choose **Start from Scratch**.

The following sections used to configure your Skill can be found using the menu tree on the left-hand side of the screen.

### Invocation

This is the phrase that will be used to invoke your Skill on Alexa.  This can be changed to whatever you would like, although if you do change it you may also want to change the "speech_text" line in the Python script to remain consistent.

![Invocation](https://github.com/nz1o/pi-scripts/blob/8d7d488d98c62568f80f790cfc38a1af2e4f5161/images/Alexa%20Endpoint.png)

### Intent

This section defines the core functionality of your Alexa Skill.  From the Intents page, you will need to create a new Intent by clicking **+ Add Intent**.  Your custom intent name must be **ShackPower**.  Once you have created the Intent, you will need to create a new Slot Type, so jump down to the next section **Slot Types** and come back here once you have added the new type.

Once you have created your Slot Type you need to associate the Slot with your Intent.  From **Intents** > **ShackPower**, scroll down to the Intent Slots section.  Create a new Intent Slot named **power_state** and select your **power_state** slot from **Slot Type**.

Finally, you will need to provide some Sample Utterances to tell Alexa how this Skill will be envoked from your device.  As you can see, I used phrases like "turn the shack power on" and "turn on the shack power".  You will notice that we use the **{power_state}** variable to indicate where we should extract our Slot from the command.  You can use any utterances you like here, just make sure you include the **{power_state}** variable somewhere in each one.

![Intent](https://github.com/nz1o/pi-scripts/blob/8d7d488d98c62568f80f790cfc38a1af2e4f5161/images/Alexa%20Intent.png)

### Slot Type

A Slot Type creates a variable placeholder that you will use to pass values from your Alexa Skill to the Python script (in this case, either ON or OFF).  From the Slot Types page, you will need to create a new Slot Type by clicking **+ Slot Type**.   Select **Create a custom slot type with values**, name your Slot Type **power_state**, and click **Next**.  On the next page, define two new values, **on** and **off**.  Now you're ready to finish creating your Intent.

![Slot Type](https://github.com/nz1o/pi-scripts/blob/8d7d488d98c62568f80f790cfc38a1af2e4f5161/images/Alexa%20Slot%20Type.png)

### Endpoint 

Finally, you need to create an Endpoint your Skill will use to connect back to your Flask application to turn your shack power on and off.   For the URL, enter the domain name that can be used to connect to your Flask application.  If you don't have a domain name associated with your home IP address, no problem, you can use a free dynamic DNS service like https://www.duckdns.org/ to create one.

For your SSL certificate, select **I will upload a self-signed certificate in X 509 format** and upload the self-signed certificate you created for your Flask application using openssl.

![Endpoint](https://github.com/nz1o/pi-scripts/blob/8d7d488d98c62568f80f790cfc38a1af2e4f5161/images/Alexa%20Endpoint.png)

### Building your Skill

Once you have finished configuring your Skill, click **Build Model** at the top of the screen.  If all goes well, your new Skill should build and be available on your Alexa devices.  

I believe that about covers it.  If I missed any steps, if anything is incorrect, or you run in to any issues please let me know: john@**\_mycallsign\_**.com

NZ1O
