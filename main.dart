import 'dart:io';

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  String? imagePath;

  Future<void> choosePicture() async {
    final picker = ImagePicker();
    final pickerFile = await picker.pickImage(source: ImageSource.camera);

    if (pickerFile != null) {
      setState(() {
        imagePath = pickerFile.path;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Camera Test'),
          actions: [
            IconButton(
              onPressed: choosePicture,
              icon: const Icon(Icons.photo),
            ),
          ],
        ),
        body: Container(
          padding: const EdgeInsets.all(12.0),
          child: Center(
            child: imagePath != null ? Image.file(File(imagePath!)) : const Text('이미지가 선택되지 않았습니다.'),
          ),
        ),
      ),
    );
  }
}
