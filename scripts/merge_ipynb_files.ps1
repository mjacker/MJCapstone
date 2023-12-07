
$arrayfiles = New-Object System.Collections.ArrayList

for ($i = 1; $i -lt 6; $i=$i+1)
{
    $file = Get-ChildItem ..\$i*.ipynb 

    if ($file -ne $null) {
        $text = " '" + $file + "' "
        $arrayfiles.Add($text) | out-null
    }
}

write-output "nbmerge $arrayfiles > ..\0_merged_ipynb_files_for_google_colab.ipynb" > runmerge.ps1
& "$PSScriptRoot\runmerge.ps1"
remove-item runmerge.ps1
