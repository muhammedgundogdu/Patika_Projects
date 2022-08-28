<?php

function ucgenCiz($sayi){
    for ($i=0;$i<=$sayi;$i++){

        $j=0;
        while ($j<=$i){
            $j++;
            echo $j*0;
        }

        echo "<br>";
    }
}

ucgenCiz(15);
