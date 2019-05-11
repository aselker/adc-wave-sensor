clearvars -except x y
fs = 115.99;
newDataLength = 5000;
newFs = fs*(newDataLength/length(x));
bitrate = 1;

freqData = fftshift(abs(fft(x)));
freq = linspace(-fs/2,fs/2,length(freqData));
[~,zeroFreq] = max(freqData);
freq = freq - freq(zeroFreq);
clf
hold off
plot(freq,freqData,'k')
[val,ind] = max(freqData(freq~=0));
carrierFreq = abs(freq(ind));
if range(x)>=range(y)
    data = x;
else
    data = y;
end

moreData = interp1((1:length(data))/fs,data,(linspace(1,length(data),newDataLength)/fs),'spline')';
moreFreqData = fftshift(abs(fft(moreData)));
moreFreq = linspace(-fs/2,fs/2,length(moreFreqData));
[~,zeroFreq] = max(moreFreqData);
moreFreq = moreFreq - moreFreq(zeroFreq);
figure
plot(1:length(moreData),moreData,'b')
time = [1:length(moreData)]./newFs;
demod = moreData.*cos(carrierFreq.*2.*pi.*time');
freqDemod = fftshift(abs(fft(demod)));
figure
plot(time,demod,'c')

widthFilter = 3;
lengthFilter = 5;
Filter = sinc(widthFilter*(-lengthFilter:(1/newFs):lengthFilter));
timeDomainSignal = conv(Filter,demod);

timeDomainSignal = timeDomainSignal(lengthFilter*newFs:end-lengthFilter*newFs);
shiftSignal = timeDomainSignal - mean(timeDomainSignal);
zeroXings = [];
bitXings = [];
for i = 2:length(shiftSignal)
    if sign(shiftSignal(i)) ~= sign(shiftSignal(i-1))
        zeroXings = [zeroXings,i];
        bitXings = [bitXings,zeroXings(1,1)+ (1/(bitrate)*newFs)*(length(zeroXings))];
    end
end
bitXings = [zeroXings(1,1),bitXings(:,1:end-1)];
output = [];
for j = 2:length(zeroXings)
    output = [output,sign(mean(shiftSignal(zeroXings(j-1):zeroXings(j),1)))];
end
figure
plot([1:length(shiftSignal)]./newFs,shiftSignal,'k')
hold on
plot(zeroXings/newFs,zeros(length(zeroXings),1),'o')
plot(bitXings/newFs,zeros(length(bitXings),1),'o')