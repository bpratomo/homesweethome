var iframe = document.getElementsByTagName('iframe')[0];
var innerDoc = iframe.contentDocument || iframe.contentWindow.document;


function checkIframeLoaded() {
    // Get a handle to the iframe element
    
    var relayoutEventDiv  = innerDoc.getElementById('relayout-data-event');

    // Check if loading is complete
    if (relayoutEventDiv) {
        afterLoading();
        return;
    } 

    // If we are here, it is not loaded. Set things up so we check   the status again in 100 milliseconds
    window.setTimeout(checkIframeLoaded, 100);
};


afterLoading = function(){
        console.log('document loaded')

        // Set the config and elements

        var observerConfig = { attributes: true, childList: true, subtree: true };



        var relayoutEventDiv  = innerDoc.getElementById('relayout-data-event');
        var clickEventDiv     = innerDoc.getElementById('click-data-event');
        var selectEventDiv    = innerDoc.getElementById('selected-data-event');

        // Observe the change 
        const relayoutCallback = function(mutationsList,observer){
            console.log(mutationsList);
            var payload = {
                "event_type":'relayout',
                "xvar":'price',
                "yvar":'area',
                "event_data":relayoutEventDiv.innerHTML
            };
            update_gallery(payload);
            console.log(payload)
        };

        const clickCallback = function(mutationsList,observer){
            console.log(mutationsList);
            var payload = {
                "event_type":'click',
                "event_data":clickEventDiv.innerHTML
            };

            update_gallery(payload);
            console.log(payload)
        };


        const selectCalback = function(mutationsList,observer){
            console.log(mutationsList);
            var payload = {
                "event_type":'select',
                "event_data":selectEventDiv.innerHTML
            };
            update_gallery(payload);
            console.log(payload);
        };


        const relayoutObserver = new MutationObserver(relayoutCallback);
        const clickObserver = new MutationObserver(clickCallback);
        const selectObserver = new MutationObserver(selectCalback);

        relayoutObserver.observe(relayoutEventDiv, observerConfig);
        clickObserver.observe(clickEventDiv, observerConfig);
        selectObserver.observe(selectEventDiv, observerConfig);
};



document.onload = checkIframeLoaded()
