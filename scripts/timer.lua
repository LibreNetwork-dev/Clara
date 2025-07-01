function sleep (a) 
    local s = tonumber(os.clock() + a); 
    while (os.clock() < s) do 
    end 
end

function setTimer(sec, min, hr) 
    local stime = sec + (min * 60) + (hr * 60 * 60) 
    sleep(stime)
    os.execute(string.format([[
        dbus-send --session \
        --dest=org.freedesktop.Notifications \
        --type=method_call \
        /org/freedesktop/Notifications \
        org.freedesktop.Notifications.Notify \
        string:"Clara" \
        uint32:0 \
        string:"clock" \
        string:"Your timer is finished" \
        string:"" \
        array:string: \
        dict:string:variant: \
        int32:5000
    ]]))
    os.execute(
        "play -n synth 2 sine 500"
    )
end 