printf("")

function newv = unitVector (v1)

       
 mag = norm(v1)
   if(mag==0)
     newv = zeros(length(v1))
   endif
     
  for i = 1:length(v1)
	    x = (v1(i))/mag;
            newv(i) = x;   
   endfor
 endfunction
   vector1 = [0,0,0]
 unitVector(vector1)
 

  
