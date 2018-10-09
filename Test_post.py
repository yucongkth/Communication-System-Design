from Client_post import Do_post

nfm_data = {

        "link_utilization": {
            "id1":"10",
            "id2":"20",
            "id3":"30"
            }
    ,

        "packet_loss": {
            "id1":"40",
            "id2":"50",
            "id3":"60"
            }
    ,
        "timestamp": "8"
    }

POSTdata=Do_post("http://127.0.0.1:2500/",nfm_data).post()
