fs = 116.81;
freq = [-fs/2:fs/2]';
freqData = fftshift(abs(fft(x,116)));
[val,ind] = max(freqData(freq~=0));
carrierFreq = freq(ind);
if range(x)>=range(y)
    data = x;
else
    data = y;
end
moreData = interp1((1:length(data))/116.38,data,(linspace(1,length(data),5000)/116.38),'spline');