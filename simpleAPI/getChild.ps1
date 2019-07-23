function getDir {
    # param (
    #     OptionalParameters
    # )
    $res=get-childitem "C:\Users\eric.travers.POLIRIS\" | ?{ $_.PSIsContainer } | Select-Object -exp Name
    return ,$res
}


