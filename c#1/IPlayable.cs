﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentValidation
{


    interface IPlayable
    {
        public void Play();
    }
    class MusicPlayer : IPlayable
    {
        public void Play()
        {
            Console.WriteLine("Playing music");
        }
    }
    class VideoPlayer : IPlayable
    {
        public void Play()
        {
            Console.WriteLine("Playing video");
        }
    }
}
