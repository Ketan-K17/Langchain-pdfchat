<script lang="ts">
	import '../app.css';
	import 'material-icons/iconfont/material-icons.css';
	import { onMount } from 'svelte';
	import Navbar from '$c/Navbar.svelte';
	import ErrorModal from '$c/ErrorModal.svelte';
	import { getUser, auth } from '$s/auth';

	export const ssr = false;

	$: user = $auth.user;

	onMount(() => {
		if (user === null) {
			getUser();
		}
	});
</script>

<ErrorModal />
<div class="container mx-auto h-screen">
	<Navbar />
	<slot />
</div>

<script context="module" lang="ts">
	import { auth } from '$s/auth';
	import { redirect } from '@sveltejs/kit';

	export const load = async ({ session }) => {
		if (!session.user) {
			throw redirect(302, '/documents');
		}
	};
</script>