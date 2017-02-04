import speech_recognition as sr
r = sr.Recognizer()
m = sr.Microphone()
#set threhold level
with m as source: r.adjust_for_ambient_noise(source)
print("Set minimum energy threshold to {}".format(r.energy_threshold))
# obtain audio from the microphone

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

print(r.recognize_google(audio))

# def internet_on():
# 	print "Checking Internet Connection"
# 	try:
# 		r =requests.get('https://api.amazon.com/auth/o2/token')
# 		print "Connection OK"
# 		return True
# 	except:
# 		print "Connection Failed"
# 		return False

# def web_service():
# 	global wit_ai_received
#
# 	# Call the two speech recognitions services in parallel
# 	alexa_thread = Thread( target=alexa, args=() )
# 	wit_ai_thread = Thread( target=wit_ai, args=( ) )
#
# 	alexa_thread.start()
# 	wit_ai_thread.start()
#
# 	# Prioritize a response from Wit.ai
# 	wit_ai_thread.join()
#
# 	# See if Wit.ai code handled response
# 	if wit_ai_received != True:
# 		# Wait until Alexa code handles response
# 		alexa_thread.join()
#
# 		# Play Alexa response
# 		os.system('play  -c 1 -r 24000 -q {}response.mp3  > /dev/null 2>&1'.format(path))
# 		time.sleep(.5)
#
#
# while internet_on() == False:
# 	print "."
#
# offline_speak("Hello "+username+", Ask me any question")
#
# print "Debug: Ready to receive request"
# while True:
# 	try:
# 		# Read from microphone
# 		l,buf = inp.read()
# 	except:
#                 # Hopefully we read fast enough to avoid overflow errors
# 		print "Debug: Overflow"
# 		continue
#
# 	#Process microphone audio via PocketSphinx only when trigger word
# 	# hasn't been detected
# 	if buf and record_audio == False:
# 		decoder.process_raw(buf, False, False)
#
# 	# Detect if keyword/trigger word was said
# 	if record_audio == False and decoder.hyp() != None:
# 		# Trigger phrase has been detected
# 		record_audio = True
# 		start = time.time()
#
# 		# To avoid overflows close the microphone connection
# 		inp.close()
#
# 		# Open file that will be used to save raw micrphone recording
# 		recording_file = open(filename_raw, 'w')
# 		recording_file.truncate()
#
# 		# Indicate that the system is listening to request
# 		offline_speak("Yes")
#
# 		# Reenable reading microphone raw data
# 		inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
# 		inp.setchannels(1)
# 		inp.setrate(16000)
# 		inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
# 		inp.setperiodsize(1024)
#
# 		print ("Debug: Start recording")
#
#
# 	# Only write if we are recording
# 	if record_audio == True:
# 		recording_file.write(buf)
#
# 	# Stop recording after 5 seconds
# 	if record_audio == True and time.time() - start > 5:
# 		print ("Debug: End recording")
# 		record_audio = False
#
# 		# Close file we are saving microphone data to
# 		recording_file.close()
#
# 		# Convert raw PCM to wav file (includes audio headers)
# 		os.system("sox -t raw -r 16000 -e signed -b 16 -c 1 "+filename_raw+" "+filename+" && sync");
#
# 		print "Debug: Sending audio to services to be processed"
# 		# Send recording to our speech recognition web services
# 		web_service()
#
# 		# Now that request is handled restart audio decoding
# 		decoder.end_utt()
# 		decoder.start_utt()
