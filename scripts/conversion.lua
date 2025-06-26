local conversion_factors = {
    -- length
    m_to_f = 3.28084,
    f_to_m = 0.3048,
    i_to_f = 1/12,
    f_to_i = 12,
    mi_to_f = 5280,
    f_to_mi = 1/5280,
    i_to_mi = 1/63360,
    mi_to_i = 63360,
  
    -- volume
    l_to_ml = 1000,
    ml_to_l = 1/1000,
    l_to_gal = 0.264172,
    gal_to_l = 3.78541,
  
    -- weight
    kg_to_lb = 2.20462,
    lb_to_kg = 0.453592,
}
  
function convert(value_str, from_unit, to_unit)
    local value = tonumber(value_str)
    if not value then return nil, "Invalid numeric value" end

    local key = from_unit:lower() .. "_to_" .. to_unit:lower()
    local factor = conversion_factors[key]
    if not factor then return nil, "Unsupported conversion: " .. from_unit .. " to " .. to_unit end
        -- copy the result to the clipboard
    os.execute(string.format(
        "echo -n '%s' | (command -v wl-copy &>/dev/null && wl-copy || xclip -selection clipboard)", 
        tostring(value * factor)
    ))
end
