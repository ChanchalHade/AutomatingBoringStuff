{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, Mary\n",
      "Access granted.\n"
     ]
    }
   ],
   "source": [
    "name = 'Mary'\n",
    "password = 'swordfish'\n",
    "if name == 'Mary':\n",
    "    print('Hello, Mary')\n",
    "    if password == 'swordfish':\n",
    "        print('Access granted.')\n",
    "    else:\n",
    "        print('Wrong password.')        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Unlike you Alice is not an undead, immortal vampire.\n"
     ]
    }
   ],
   "source": [
    "name = 'Carol'\n",
    "age = 3000\n",
    "if name == 'Alice':\n",
    "    print('Hi, Alice.')\n",
    "elif age < 12:\n",
    "    print('You are not Alice, kiddo.')\n",
    "elif age > 2000:\n",
    "    print('Unlike you Alice is not an undead, immortal vampire.')\n",
    "elif age > 100:\n",
    "    print('You are not Alice, grannie.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You are not Alice, grannie.\n"
     ]
    }
   ],
   "source": [
    "name = 'Carol'\n",
    "age = 3000\n",
    "if name == 'Alice':\n",
    "    print('Hi, Alice.')\n",
    "elif age < 12:\n",
    "    print('You are not Alice, kiddo.')\n",
    "elif age > 100:\n",
    "    print('You are not Alice, grannie.')    \n",
    "elif age > 2000:\n",
    "    print('Unlike you Alice is not an undead, immortal vampire.')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You are neither Alice nor a little kid.\n"
     ]
    }
   ],
   "source": [
    "name = 'Carol'\n",
    "age = 3000\n",
    "if name == 'Alice':\n",
    " print('Hi, Alice.')\n",
    "elif age < 12:\n",
    " print('You are not Alice, kiddo.')\n",
    "else:\n",
    " print('You are neither Alice nor a little kid.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, world.\n"
     ]
    }
   ],
   "source": [
    "spam=0\n",
    "if spam<5:\n",
    "    print('Hello, world.')\n",
    "    spam=spam+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, world.\n",
      "Hello, world.\n",
      "Hello, world.\n",
      "Hello, world.\n",
      "Hello, world.\n"
     ]
    }
   ],
   "source": [
    "spam=0\n",
    "while spam<5:\n",
    "    print('Hello, world.')\n",
    "    spam=spam+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is\n",
      "Jimmy Five Times (0)\n",
      "Jimmy Five Times (1)\n",
      "Jimmy Five Times (2)\n",
      "Jimmy Five Times (3)\n",
      "Jimmy Five Times (4)\n"
     ]
    }
   ],
   "source": [
    "print('My name is')\n",
    "for i in range(5):\n",
    " print('Jimmy Five Times (' + str(i) + ')')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is\n",
      "Jimmy five times(0)\n",
      "Jimmy five times(1)\n",
      "Jimmy five times(2)\n",
      "Jimmy five times(3)\n",
      "Jimmy five times(4)\n"
     ]
    }
   ],
   "source": [
    "print('My name is')\n",
    "for i in range(5):\n",
    "    print('Jimmy five times('+ str(i)+')')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "18\n",
      "16\n",
      "14\n",
      "12\n",
      "10\n",
      "8\n",
      "6\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "for i in range(20,2,-2):\n",
    "    print(i)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "for i in range(5,11,1):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "4\n",
      "2\n",
      "10\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "for i in range(5):\n",
    "    print(random.randint(1,10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
