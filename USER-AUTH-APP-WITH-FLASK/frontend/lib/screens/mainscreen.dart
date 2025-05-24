import 'package:flutter/material.dart';
import 'package:frontend/services/api_service.dart';

class MainScreen extends StatefulWidget {
  const MainScreen({super.key, required this.token});

  final String token;
  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  String? username;
  int? age;
  String? role;
  bool isLoading = true;

  @override
  void initState() {
    super.initState();
    loadProfile();
  }

  Future<void> loadProfile() async {
    final profile = await ApiService.getProfile(widget.token);
    if (profile != null) {
      setState(() {
        username = profile['username'];
        age = profile['age'];
        role = profile['role'];
        isLoading = false;
      });
    } else {
      setState(() {
        username = 'Error';
        age = 0;
        role = 'Unknown';
        isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Main Screen')),
      body:
          isLoading
              ? const Center(child: CircularProgressIndicator())
              : Center(
                child: Column(
                  children: [
                    Text(
                      '👤 Username: $username',
                      style: const TextStyle(fontSize: 20),
                    ),
                    Text('🎂 Age: $age', style: const TextStyle(fontSize: 20)),
                    Text(
                      '🧾 Role: $role',
                      style: const TextStyle(fontSize: 20),
                    ),
                  ],
                ),
              ),
    );
  }
}
