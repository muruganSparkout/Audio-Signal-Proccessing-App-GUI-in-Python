from AudioLib.AudioProcessing import AudioProcessing


class AudioEffect(object):
    __slots__ = ()

    @staticmethod
    def echo(input_path, output_path):
        # Applies an echo effect to a given input audio file
        sound = AudioProcessing(input_path)
        sound.set_echo(0.09)
        sound.save_to_file(output_path)
